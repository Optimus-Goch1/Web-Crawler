from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang ="en">
<head>
    <meta =charset= "UTF-8">
    <title>First HTML Page</title>
</head>
<body>
    <div id = "first">
    <h3 data example = "yes">hi</h3>
    <p>more text.</p>
    </div>
    <ol>
        <li class="special">This item is special.</li>
        <li class="special"> This item is also special.</li>
        <li>This item is not special</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
d = soup.select(".special")[]
print(d.get_text())
