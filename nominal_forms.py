import devtrans
import re
def iast_to_dev(string:str):
    return devtrans.slp2dev(devtrans.iast2slp(string))

def process_string(string):
   """Processes a string, applying iast_to_dev only to non-HTML parts.

   Args:
       string: The input string.
       iast_to_dev: A function that takes a string as input and returns the transformed string.

   Returns:
       The processed string with iast_to_dev applied to non-HTML parts.
   """

   parts = re.split(r"(<[^>]*>)", string)  # Split string into HTML and non-HTML parts
   output = []

   for part in parts:
       if re.match(r"<[^>]*>", part):  # Check if it's an HTML part
           output.append(part)  # Append HTML part as is
       else:
           output.append(iast_to_dev(part))  # Apply iast_to_dev to non-HTML part

   return "".join(output)

def get_nominal_form(singular, dual, plural, convert_to_devanagari):
    singular = singular
    dual = dual
    plural = plural
    if convert_to_devanagari:
        for i in range(len(singular)):
            singular[i]= process_string(singular[i])
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


