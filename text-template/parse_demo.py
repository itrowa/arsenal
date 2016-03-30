import re

e1 = "abc.edf.ghi"
print(e1.split("."))



buffered = ["haha", "hehe"]
if len(buffered) == 1:
    print("append_result(%s)" % buffered[0])
elif len(buffered) > 1: 
    print("extend_result([%s])" % ", ".join(buffered))

# re对templite的解析
text = '''
    <h1>Hello {{name|upper}}! </h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    { endfor %}
    '''
tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
print(tokens)