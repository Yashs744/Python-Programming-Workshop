import webbrowser
import bs4
import requests
import argparse
import os

parser = argparse.ArgumentParser(description='Search Item on Youtube')
parser.add_argument('search', metavar='search_item', type=str, nargs='+', help='Search the item on Youtube')
parser.add_argument('N', metavar="N", type=str, nargs='+', help="Number of Videos to Display")

args = parser.parse_args()


def searchYoutube():
	n = int(''.join(args.N))
	url = 'https://www.youtube.com/results?search_query=' + ' '.join(args.search)

	res = requests.get(url)
	soup = bs4.BeautifulSoup(res.text, "lxml")
	linkElems = soup.findAll('h3', {'class':'yt-lockup-title '})

	numOpen = min(n, len(linkElems))

	link = []
	print ("List of YouTube Videos: ")
	for i in range(numOpen):
		link.append(linkElems[i].find('a')['href'])
	for i in range(numOpen):
		print(str(i+1)+'. '+linkElems[i].find('a').text)

	while True:
		try:
			userChoice = int(input('\nEnter Video Number to Open: '))

			if userChoice not in range(1,n):
				print('Enter Correct Number')
				continue
			break

		except NameError:
			print('Enter Correct Number')
			continue

	print("Downloading")
	os.system("youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best " + 'https://www.youtube.com'+link[userChoice-1])

	webbrowser.open('https://www.youtube.com/'+link[userChoice-1])

if __name__ == '__main__':
	searchYoutube()
