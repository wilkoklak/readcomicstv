import requests
import os

print('ReadComicsTV Download\n')
print('Give comic URL name (ex. old-man-logan): ')
name = input('http://readcomics.tv/images/manga/ + : ')
base_url = 'http://readcomics.tv/images/manga/' + name + '/{}/{}.jpg'
issues = input('Number of issues to download (can also be range, like 5-20): ')
issues = issues.split('-')
if len(issues) == 1:
	issues = [1, int(issues[0])]
try:
	os.mkdir('downloads')
except FileExistsError:
	pass
try:
	os.mkdir(os.path.join('downloads', name))
except FileExistsError:
	pass

for issue in range(int(issues[0]), int(issues[1]) + 1):
	print('Downloading issue #{}...'.format(issue))
	try:
		os.mkdir(os.path.join('downloads', name, str(issue)))
	except FileExistsError:
		pass
	page = 1
	while True:
		print('Page {}...\t\t'.format(page), end='\r')
		r = requests.get(base_url.format(issue, page))
		if r.status_code == 200:
			raw = r.content
			with open(os.path.join('downloads', name, str(issue), '{}.jpg'.format(page)), 'wb+') as img:
				img.write(raw)
		else:
			break
		page += 1
	print('Finished downloading issue #{}'.format(issue))
