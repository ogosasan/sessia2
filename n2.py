from flask import Flask, render_template, request

app = Flask(__name__)

def delete(line):
    lst = []
    for i in line:
        if i not in lst:
            lst.append(i)
    return ''.join(lst)

@app.route('/', methods = ['GET', 'POST'])
def test():
    line = request.form.get('txt')
    answer = ''
    if request.method == 'POST':
        answer = delete(line)
    return render_template('n2.html', string = answer)

if __name__ == '__main__':
    app.run()