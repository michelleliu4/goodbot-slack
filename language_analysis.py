import requests
from requests.exceptions import ConnectionError
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.api_core.exceptions import InvalidArgument
import six
import sys
import re

# User indicates upload method
print('-' * 20)
print('Uploading content directly? (direct)')
print('')
decision = input('Enter upload type: ')

# Handles content entered directly into .txt file
if decision == 'direct':
    while True:
        print('-' * 20)
        print('Choose an analysis to run:')
        print('')
        print('Run Sentiment Analysis? (A)')
        print('Run Content Classification? (B)')
        print('Run Entities Analysis? (C)')
        print('Run Entity Sentiment Analysis? (D)')
        print('Run Syntax Analysis? (E)')
        print('-' * 20)
        print('')

        # Each analysis will correspond with a letter from the list above.
        choice = input('Which Analysis to Run? ')

        # Content Classification (gnl-classify.content.py)
        if choice == 'B' or choice == 'b':

            with open('gnl-direct-check.txt', 'r') as gnl:
                content = gnl.read()
                content = str(content)

                downloadFile = 'gnl-content-direct.csv'
                file = open(downloadFile, 'w')
                columnHead = 'String,Type,Confidence\n'
                file.write(columnHead)
                
                def classify_text(text):

                    client = language.LanguageServiceClient()

                    if isinstance(text, six.binary_type):
                        text = text.decode('utf-8')

                    document = types.Document(
                        content=text.encode('utf-8'),
                        type=enums.Document.Type.PLAIN_TEXT)

                    categories = client.classify_text(document).categories

                    for category in categories:
                        print(u'{:<16}: {}'.format('type', category.name))
                        print(u'{:<16}: {}'.format(
                            'confidence', category.confidence))
                        print(u'{:<16}: {}'.format('content', content) + '\n')
                        print('')
                        
                        row = f'"{content}",{category.name},{category.confidence}\n'
                        file.write(row)
                    file.close()
                        
                try:
                    classify_text(content)
                except InvalidArgument as e:
                    print(f'{e}')

        # Sentiment Analysis (google-natural-language-api.py)
        if choice == 'A' or choice == 'a':

            with open('gnl-direct-check.txt', 'r') as gnl:
                downloadFile = 'gnl-sentiment-direct.csv'
                file = open(downloadFile, 'w')
                content2 = gnl.read()

                columnHead = 'Content,Sentiment Score,Sentiment Magnitude\n'
                file.write(columnHead)

                # Instantiates a client
                client = language.LanguageServiceClient()

                document = types.Document(
                    content=content2,
                    type=enums.Document.Type.PLAIN_TEXT)

                # Detects the sentiment of the text
                sentiment = client.analyze_sentiment(
                    document=document).document_sentiment

                print('Content: {}'.format(content2))
                print('Sentiment: {}, {}'.format(
                    sentiment.score, sentiment.magnitude))

                row = f'"{content2}",{sentiment.score},{sentiment.magnitude}\n'
                file.write(row)
                file.close()

        # Entity Sentiment (gnl-entity-sentiment.py)
        if choice == 'D' or choice == 'd':
            with open('gnl-direct-check.txt', 'r') as gnl:
                downloadFile = 'gnl-entity-sent-direct.csv'
                file = open(downloadFile, 'w')
                content3 = gnl.read()

                columnHead = 'Name,Begin Offset,Content,Magnitude,Sentiment,Type,Salience,Sentiment\n'
                file.write(columnHead)

                def entity_sentiment_text(text):
                    """Detects entity sentiment in the provided text."""
                    client = language.LanguageServiceClient()

                    if isinstance(text, six.binary_type):
                        text = text.decode('utf-8')

                    document = types.Document(
                        content=text.encode('utf-8'),
                        type=enums.Document.Type.PLAIN_TEXT)

                    #  Detect and send native Python encoding to receive correct word offsets.
                    encoding = enums.EncodingType.UTF32
                    if sys.maxunicode == 65535:
                        encoding = enums.EncodingType.UTF16

                    result = client.analyze_entity_sentiment(document, encoding)

                    for entity in result.entities:
                        print('Mentions: ')
                        print(u'Name: "{}"'.format(entity.name))
                        for mention in entity.mentions:
                            print(u'  Begin Offset : {}'.format(
                                mention.text.begin_offset))
                            print(u'  Content : {}'.format(mention.text.content))
                            print(u'  Magnitude : {}'.format(
                                mention.sentiment.magnitude))
                            print(u'  Sentiment : {}'.format(
                                mention.sentiment.score))
                            print(u'  Type : {}'.format(mention.type))
                            print(u'Salience: {}'.format(entity.salience))
                            print(u'Sentiment: {}\n'.format(entity.sentiment))

                            row = f'"{entity.name}",{mention.text.begin_offset},{mention.text.content},' \
                                f'{mention.sentiment.magnitude},{mention.sentiment.score},{mention.type},' \
                                f'{entity.salience},{entity.sentiment}\n'
                            file.write(row)
                    file.close()
                entity_sentiment_text(content3)

        # Entity Analysis (gnl-entities.py)
        if choice == 'C' or choice == 'c':
            with open('gnl-direct-check.txt', 'r') as gnl:
                downloadFile = 'gnl-entity-analysis-direct.csv'
                file = open(downloadFile, 'w')
                content4 = gnl.read()
                columnHead = 'Name,Type,Salience,Wikipedia URL,MID\n'
                file.write(columnHead)

                client = language.LanguageServiceClient()

                if isinstance(content4, six.binary_type):
                    content4 = content4.decode('utf-8')

                # Instantiates a plain text document.
                document = types.Document(
                    content=content4,
                    type=enums.Document.Type.PLAIN_TEXT)

                # Detects entities in the document. You can also analyze HTML with:
                # Document.type == enums.Document.Type.HTML
                entities = client.analyze_entities(document).entities

                for entity in entities:
                    entity_type = enums.Entity.Type(entity.type)
                    print('=' * 20)
                    print(u'{:<16}: {}'.format('name', entity.name))
                    print(u'{:<16}: {}'.format('type', entity_type.name))
                    print(u'{:<16}: {}'.format('salience', entity.salience))
                    print(u'{:<16}: {}'.format('wikipedia_url', entity.metadata.get('wikipedia_url', '-')))
                    print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))

                    row = f'{entity.name},{entity_type.name},{entity.salience},{entity.metadata.get("wikipedia_url")},\
                    {entity.metadata.get("mid")}\n'
                    file.write(row)
                file.close()