n = int(input())

htmls = []

# HTML CODE	<HTML>BODY</HTML>
# BODY	<BODY>TEXT</BODY>
# TEXT	STRING | STRING TEXT | TAG | TAG TEXT
# STRING	possibly empty string of printable characters other than '<' and '>')
# TAG	BOLD | ITALICS | LINK
# BOLD	<B>TEXT</B>
# ITALICS	<I>TEXT</I>
# LINK	<A HREF=URL>TEXT</A>
# URL	http://STRING.com

for i in range(n):
  htmls.append(list(map(str,input().split())))

for i in range(n):
  print(htmls[i])