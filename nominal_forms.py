import devtrans
import re
def iast_to_dev(string:str):
    return devtrans.slp2dev(devtrans.iast2slp(string))


import re

import re


def process_string(input_string):
    # Regular expression to find markdown links and HTML tags
    markdown_and_html_pattern = r'(\[([^\]]+)\]\((.*?)\)|<[^>]+>)'

    # Find all markdown links and HTML tags in the input string
    matches = re.finditer(markdown_and_html_pattern, input_string)

    # Initialize variables
    processed_string = ''
    last_index = 0

    # Iterate through matches
    for match in matches:
        start, end = match.span()

        # Process the text before the current match
        processed_string += iast_to_dev(input_string[last_index:start])

        # Check if the match is a markdown link
        if input_string[start] != '<':
            # Process the text inside square brackets of the markdown link
            link_text_start = start + 1
            link_text_end = input_string.find(']', link_text_start, end)
            processed_string += '[' + iast_to_dev(input_string[link_text_start:link_text_end]) + ']'
            processed_string += input_string[link_text_end + 1:end]
        else:
            # Add the match without processing if it's an HTML tag
            processed_string += input_string[start:end]

        # Update last index
        last_index = end

    # Process the remaining text after the last match
    processed_string += iast_to_dev(input_string[last_index:])
    print(processed_string)
    return processed_string

def get_nominal_form(singular, dual, plural, convert_to_devanagari):
    singular = singular
    dual = dual
    plural = plural
    if convert_to_devanagari:
        for i in range(len(singular)):
            singular[i] = process_string(singular[i])
        for i in range(len(dual)):
            dual[i] = process_string(dual[i])
        for i in range(len(plural)):
            plural[i] = process_string(plural[i])


    stem = f"""
    |**Case**| Singular | Dual | Plural|  
    |-|-|-|-|  
    |**Nominative** (Subject)|{singular[0]}|{dual[0]}| {plural[0]}|
    |**Accusative** (Object)|{singular[1]}|{dual[0]}| {plural[1]}|
    |**Instrumental** (By/With)|{singular[2]}|{dual[1]}| {plural[2]}|
    |**Dative** (For)|{singular[3]}|{dual[1]}| {plural[3]}|
    |**Absolutive** (From)|{singular[4]}|{dual[1]}| {plural[3]}|
    |**Genitive** (Of)|{singular[5]}|{dual[2]}| {plural[4]}|
    |**Locative** (In/On)|{singular[6]}|{dual[2]}| {plural[5]}|
    |**Vocative** (Addressing)|{singular[7]}|{dual[0]}| {plural[0]}|
    """
    return stem


