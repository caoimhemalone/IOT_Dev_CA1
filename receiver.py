import dweepy

thingName="CaoimhesThing";

for dweet in dweepy.listen_for_dweets_from('CaoimhesThing'):
	print dweet