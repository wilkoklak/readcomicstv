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
		h = requests.head(base_url.format(issue, page))
		if h.status_code == 200:
			total = round(int(h.headers['Content-Length']) / (1024*1024), 2)
			current = 0
			r = requests.get(base_url.format(issue, page), stream=True)
			last_msg = ''
			with open(os.path.join('downloads', name, str(issue), '{}.jpg'.format(page)), 'wb+') as img:
				for chunk in r.iter_content(chunk_size=4096):
					clear = len(last_msg) * " " + " "
					current += len(chunk) / (1024*1024)
					img.write(chunk)
					last_msg = '\rPage #{} progress: {} of {} MB'.format(page, round(current, 2), total)
					print(clear + last_msg, end='\r')
				img.close()
		else:
			break
		page += 1
	print('Finished downloading issue #{}'.format(issue))
