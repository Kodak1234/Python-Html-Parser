"""
Lightweight html parser. Text structure is not maintained and tags are passed in the other they were encountered by the program
 so parsing multiple tags could mix up text from each tag.

Author Umeugwa Dabeluchi

Date September 29, 2016

"""

class HttpParser(object):
    def __init__(self, options):
        self.HttpOption = options
        self.response = None
        self.message = self.HttpOption.message
        self.decode()

    """
    This function go through the message looking for an opening html tag.
            
    """
    def parse(self):
        counter = 0
        self.response = ""

        while(counter < len(self.message)):
            if(ord(self.message[counter]) == ord('<')):
                if(self.message[counter+1] == "/"):#closing tag, so continue
                    counter += 1
                    continue
                
                tag,counter = self.getTag(counter+1)
                
                if(self.HttpOption.hasTag(tag.strip())):
                    if(self.HttpOption.inside):
                        counter = self.readInside(counter)

                    else:
                        counter = self.readTag(counter)
                  #  print(self.message[counter])

            counter = counter + 1

    def decode(self):
        if(type(self.HttpOption.decode) == type("string")):
            self.message = self.message.decode(self.HttpOption.decode)

    #Not used
    def encode(self):
        if(self.HttpOption.encode != "plain"):
            self.response = self.response.encode(self.HttpOption.encode)

    def getOption(self):
        return self.HttpOption

    """
    Reads the text inside a html tag

    @param of : The offset of were to start

    @return : Returns the offset where the message ended

    """
    def readInside(self,of):
        for a in range(of,len(self.message)):
            if(ord(self.message[a]) == ord('>')):
                self.response += "\r\n"
                return a;

            self.response += self.message[a]

        return of

    """
    Reads the text between a html tag

    @param of : The offset of were to start

    @return : Returns the offset where the message ended

    """
    def readTag(self,of):
        for a in range(of,len(self.message)):
            if(ord(self.message[a]) == ord('<')):
                if(ord(self.message[a+1]) == ord('/')):

                    #Keep looping till the end of the html tag
                    while(ord(self.message[a]) != ord('>')):
                        a += 1

                    self.response += "\r\n"
                    return a

                #This a nested tag, so return so that we can pass the nested tag
                else:
                    return a - 1
            
            self.response += self.message[a] #Append to the response

        return of

    """
    Read a tag from the html message.
    
    @param of : The offset of were to start

    @returns: Returns the offset where the tag ended and the tag that was retrieved

    """
    def getTag(self,off):
        tag = " "
        append = True

        for a in range(off,len(self.message)):
            if(ord(self.message[a]) == ord('>')):
                return (tag,a+1)

            #32 is a space character
            elif(ord(self.message[a]) == 32):
                append = False
                if(self.HttpOption.inside):
                    return (tag,a)
                

            if(append):
                tag += self.message[a]

        return (tag,off)

    def getResponse(self):
        return self.response.strip()

    def __str__(self):
        return response.strip()



"""
Holds the options of what and how tags are parsed
"""
class HttpOption(object):
    def __init__(self,message):
        
        self.message = message
        self.inside = False
        self.decode = None
        self.encode = "plain"
        
        self.tags = []
        self.isHeader = False

    def hasTag(self,tag):
        return tag in self.tags;
        
        
    def isHeader(self,isHeader):
        self.isHeader = isHeader
        return self

    #Has no effect
    def encodeAs(self,encode):
        self.encode = encode
        return self

    def readInside(self,where):
        self.inside = where
        return self

    def decodeAs(self, decode):
        self.decode= decode
        return self

    def parseTag(self, tag):
        self.tags.append(tag.strip())
        return self

    def __str__(self):
        return self.message










