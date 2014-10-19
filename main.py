#<NerdCraw, an instant slashdot.org reader>
#Copyright (C) <2014> <Janith Perera>

#------------------------------------------------------------------------------
# Name     : nerdcraw/main.py
# Language : Python 2.7
# Authors  : Janith Perera, janith@member.fsf.org
# Function : Main program
# Usage    : See documentation
#------------------------------------------------------------------------------

#This file is part of NerdCraw.

#NerdCraw is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#NerdCraw is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with NerdCraw. If not, see <http://www.gnu.org/licenses/>.

import urllib
import re
import sys


def get_headings(_webpage):
    """
    Prints all the headings and handles the main
    functionality.
    """
    # condition flags declaration
    _aflag = 0
    _hflag = 0
    _h1flag = 0
    # regex patterns
    _strip1 = re.compile(r'(?<=\>)(.*)(?=</a></h1>)')
    _strip2 = re.compile(r'(?i)<a[^>]*>')
    # sequence of headings
    _seq = 1
    _cc = 1
    # url dictionary
    url = {}
    
    for lines in _webpage.readlines():
        # This section strips the headings from loaded webpage
        # and fetch them to the dictionary, which is identified by
        # a sequence. 
        if re.search("<header",lines):
            _hflag = 0
        if _hflag == 1:
            try:
                print "["+str(_seq)+"] "+re.sub(_strip2, '', _strip1.search(lines).\
                                                group())+"\n"
                url.update({_seq:_strip2.search(_strip1.search(lines).group()).group().\
                            replace('<a href=\"','http:').replace('\">','')})
                _seq += 1
                while _cc == 1:
                    if (_seq%5) == 0:
                        con = raw_input("more news available,\n do you wish to continue ?(y/n) ")
                        print "\n"
                        if con == 'y':
                            _cc = 0
                            continue
                        elif con == 'n':
                            index_in = raw_input("enter title index to load (type 'q' to abort): ")
                            if index_in != 'q':
                                # Load the sub page of a heading"
                                load_dummy(get_url(int(index_in), url)) #must change
                            else : sys.exit()
                        else:
                            print "bad answer!"
                    else:
                        _cc = 0
                _cc = 1           
            except AttributeError:
                continue
        if re.search("<header class=\"story-header\"",lines):
            _hflag = 1

def get_url(index, _url_dict):
    """
    Returns the url from the given dictionary
    """
    return _url_dict[index]

def load_dummy(_url):
    #remove this method after testing
    print _url

def load_url(_url):
    """
    Returns the web page for the given url
    """
    try:
        return urllib.urlopen(_url)
    except AttributeError: #modify this
        print "bad url!"
        sys.exit()

def intro():
    """
    Prints info header
    """
    print "\n"
    print "+-----------------------------------------------+"
    print "|                 slashdot.org                  |"
    print "+-----------------------------------------------+"
    print "\n\n"


if __name__=='__main__':
    intro()
    get_headings(load_url("http://beta.slashdot.org/"))
    
    


