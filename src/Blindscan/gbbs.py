class GigablueBlindscan:
	BINARY = "/usr/bin/gbbs"
	NIM_TYPES = ("TS3L10", "TS2L08")

	def getNimName(self, description):
		return next((x for x in self.NIM_TYPES if x in (description or "")), "")

	def isSupported(self, brand, description):
		return brand == "gigablue" and bool(self.getNimName(description))

	def getCommand(self, startFrequency, stopFrequency, startSymbolRate, stopSymbolRate, polarisation, band, frontend):
		# The helper takes an actual NIM socket, not an I2C bus or FBC index.
		return (self.BINARY, self.BINARY, str(startFrequency), str(stopFrequency), str(startSymbolRate), str(stopSymbolRate), str(polarisation % 2), str(band), str(frontend))


gigablueBlindscan = GigablueBlindscan()
