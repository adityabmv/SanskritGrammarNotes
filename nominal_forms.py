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
    return processed_string

def get_nominal_form(singular, dual, plural, convert_to_devanagari):
    t_singular = singular
    t_dual = dual
    t_plural = plural
    if convert_to_devanagari:
        for i in range(len(t_singular)):
            t_singular[i] = process_string(t_singular[i])
        for i in range(len(t_dual)):
            t_dual[i] = process_string(t_dual[i])
        for i in range(len(plural)):
            t_plural[i] = process_string(t_plural[i])


    stem = f"""
    |**Case**| Singular | Dual | Plural|  
    |-|-|-|-|  
    |**Nominative** (Subject)|{t_singular[0]}|{t_dual[0]}| {t_plural[0]}|
    |**Accusative** (Object)|{t_singular[1]}|{t_dual[0]}| {t_plural[1]}|
    |**Instrumental** (By/With)|{t_singular[2]}|{t_dual[1]}| {t_plural[2]}|
    |**Dative** (For)|{t_singular[3]}|{t_dual[1]}| {t_plural[3]}|
    |**Ablative** (From)|{t_singular[4]}|{t_dual[1]}| {t_plural[3]}|
    |**Genitive** (Of)|{t_singular[5]}|{t_dual[2]}| {t_plural[4]}|
    |**Locative** (In/On)|{t_singular[6]}|{t_dual[2]}| {t_plural[5]}|
    |**Vocative** (Addressing)|{t_singular[7]}|{t_dual[0]}| {t_plural[0]}|
    """
    return stem


