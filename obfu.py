import urllib.parse

lackofart = '''
        OBFUSCATOR
'''


def paramEncode(params="", charset="", encodeEqualSign=False, encodeAmpersand=False, urlDecodeInput=True,
                urlEncodeOutput=True):
    result = ""
    equalSign = "="
    ampersand = "&"
    if '=' and '&' in params:
        if encodeEqualSign:
            equalSign = equalSign.encode(charset)
        if encodeAmpersand:
            ampersand = ampersand.encode(charset)
        params_list = params.split("&")
        for param_pair in params_list:
            param, value = param_pair.split("=")
            if urlDecodeInput:
                param = urllib.parse.unquote(param)
                value = urllib.parse.unquote(value)
            param = param.encode(charset)
            value = value.encode(charset)
            if urlEncodeOutput:
                param = urllib.parse.quote_plus(param)
                value = urllib.parse.quote_plus(value)
            if result:
                result += ampersand
            result += param + equalSign + value
    else:
        if urlDecodeInput:
            params = urllib.parse.unquote(params)
        result = params.encode(charset)
        if urlEncodeOutput:
            result = urllib.parse.quote_plus(result)
    return result
