<h4>Python-Html-Parser</h4>
A lightweight python library for parsing html tags

<h5> Sampple html tag </h5>
m = <!--

<div class='w3-col l3 m6'>
          <h3>XML</h3>
          <p> Hey this is a sample </p>
          <li> Number one </li>
          <a href='/xml/default.asp'>Learn XML</a>
          <a href='/xsl/default.asp'>Learn XSLT</a>
          <a href='/xsl/xpath_intro.asp'>Learn XPath</a>
          <a href='/xsl/xquery_intro.asp'>Learn XQuery</a>
        </div>

-->

p = HttpOption(m) <!-- Create a HttpOption Object ->

p.parseTag("p").parseTag("a").parseTag("li") <!-- Add tags you want to pass -->

http = HttpParser(p) <!--te a HttpParser Object and pass in the HttpOption object in the constructor-->

http.parse() #Call parse() to parse the html

print(http.getResponse()) <!--t the parsed html-->

<!--rse only the elements inside a tag example  <a href="url"/> will return href = "url" after being parsed-->
p.parseTag("p").parseTag("a").parseTag("li").readInside(True) # call readInside() and pass True



