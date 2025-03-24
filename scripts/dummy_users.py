from apps.accounts.models import User


def create_dummy_users():
	first_names_male = [
		"Tim",
		"Tom",
		"Randy",
		"Frank",
		"Peter",
		"John",
		"Devin",
		"Chris",
		"Angel",
		"Stephen",
		"Brady",
		"Clarence",
		"Jacques",
		"Jason",
		"Robert",
		"Joey",
		"Sergio",
		"Rene"
	]

	first_names_female = [
		"Wendy",
		"Angelica",
		"Estella",
		"Jessica",
		"Rebecca",
		"Francine",
		"Samantha",
		"Tuesday"
		"Edna",
		"Susannah",
		"Anna",
		"Carol",
		""
	]
	# Instantiate Random Users
	a, b, c, d, e, f, g, h, i, j = User(), User(), User(), User(), User(), User(), User(), User(), User(), User()
	a.first_name, a.last_name = "Bruce", "Banner"
	b.first_name, b.last_name = "Bruce", "Wayne"
	c.first_name, b.last_name = "Billy", "Batson"
	d.first_name, b.last_name = "Carol", "Danvers"
	e.first_name, b.last_name = "Jessica", "Jones"
	f.first_name, b.last_name = "Stephen", "Strange"
	g.first_name, b.last_name = "Hank", "Pym"
	h.first_name, b.last_name = "Steve", "Rogers"
	i.first_name, b.last_name = "Wanda", "Maximoff"
	j.first_name, b.last_name = "Peter", "Parker"

	# Point towards profile pictures
	img_base_path = "/static/img/dummy/avatars/"
	a.profile_picture = img_base_path + "brucebanner.png"
	b.profile_picture = img_base_path + "brucewayne.png"
	c.profile_picture = img_base_path + "billybatson.png"
	d.profile_picture = img_base_path + "caroldanvers.png"
	e.profile_picture = img_base_path + "jessicajones.png"
	f.profile_picture = img_base_path + "stephenstrange.png"
	g.profile_picture = img_base_path + "hankpym.png"
	h.profile_picture = img_base_path + "steverogers.png"
	i.profile_picture = img_base_path + "wandamaximoff.png"
	j.profile_picture = img_base_path + "peterparker.png"

	# Create City and States
	a.city, a.state_or_province = "Richland", "Washington"
	b.city, b.state_or_province = "New York", "New York"
	c.city, c.state_or_province = "New York", "New York"
	d.city, d.state_or_province = "New York", "New York"
	e.city, e.state_or_province = "Richland", "Washington"
	f.city, f.state_or_province = "Richland", "Washington"
	g.city, g.state_or_province = "Richland", "Washington"
	h.city, h.state_or_province = "Richland", "Washington"
	i.city, i.state_or_province = "Richland", "Washington"
	j.city, j.state_or_province = "Richland", "Washington"