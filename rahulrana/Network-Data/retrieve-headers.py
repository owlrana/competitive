# to retrieve headers using python code rather than F12 and Network tab showing headers
# still writing this code, the code is broken as of now

h = get_headers(url)
if(h[0] == 200):
{
   print("Bingo!")
}