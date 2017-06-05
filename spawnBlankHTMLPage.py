f = open('src/HTML_PAGE_ELEMENTS.txt')
how_many_p_elements = input('How many paragraphs? ')
page_name = input('Give your page a name: ')
michael = f.readlines()
mimei = list(i.strip() for i in michael)
f.close()
def Create_Page():
    f = open(page_name,'a')
    for i in range(0,mimei.index("<script>")):
        f.write(mimei[i]+'\n')
    for i in range(1,int(how_many_p_elements)+1):
        f.write('<p id="{}"></p>\n'.format(i))
    for i in range(mimei.index("<script>"),len(mimei)):
        f.write(mimei[i]+'\n')
    f.close()
Create_Page()
