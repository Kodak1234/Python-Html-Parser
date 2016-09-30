# Python-Html-Parser
A lightweight python library for parsing html tags

Parsing a html file

Sample html 

#m = "<p>Test paragraph</p> <li> Number one </li> <a href =\"url\"/>"

p = HttpOption(m) #Create a HttpOption object

p.parseTag("p").parseTag("a").parseTag("li") #Add the tags you want to pass

http = HttpParser(p) #Create a HttpParser Object and pass in the HttpOption object in the constructor

http.parse() #Call parse() to parse the html

print(http.getResponse()) #Print the parsed html

To parse only the elements inside a tag example  <a href="url"/> will return href = "url" after being parsed
p.parseTag("p").parseTag("a").parseTag("li").readInside(True) # call readInside() and pass True



