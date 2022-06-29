# qbittorrent API/CLI py script.
# 
# En nem vagyok programozo se kodolo
# En probalkozok, szenvedek de legalabb mukszik

# NEM SZEP A KOD LEHETNE JOBB SZEBB - DE AZ ENYEM

qbt
	category
		add
		delete
		list
		set
		
	global
		*info 
		limit
			alternative
			download
			upload
		save-path
		
	inspect
		file
		
	network
		credentials
			add
			clear
			delete
		proxy
			reset
			set
		settings
		
	peer
		ban
		
	rss
		feed
			add
				feed
				folder
			delete
			info
			list
			move
		rule
			add
			delete
			list
			rename
			set
			
	search
		plugin
			disable
			enable
			install
			list
			uninstall
			update
		start

	server
		info
		log
		settings
			authentication
				whitelist
					clear
					delete
					list
					whitelist
			auto-tmm
			connection
			dns
			downloads
			email
			ip-filter
				add
				clear
				delete
				list
			monitored-folder
				add
				clear
				delete
				list
			privacy
			proxy
			queue
			seeding
			speed
			tracker
				add
				clear
				delete
				list
			web

	settings
		reset
			all
			password
			url
			username
		set
			password
			url
			username
	
	tag
		add
		delete
		list

	torrent
		add
			file
			url
		category
		check
		content
		delete
		file
			list
			priority
			rename
		limit
			download
			upload
		list
			move
			options
		pause
		peer
			add
			list
		peers
		pieces
		priority
			down
			max
			min
			up
		properties
		reannounce
		rename
		resume
		share

	tags
		add
		clear
		delete
		list
	
	tracker
		add
		delete
		edit
		list

	web-seeds