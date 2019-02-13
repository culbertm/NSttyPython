#
# Copyright (c) 2008-2016 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class nsparam(base_resource) :
	""" Configuration for netscaler parameters resource. """
	def __init__(self) :
		self._httpport = None
		self._maxconn = None
		self._maxreq = None
		self._cip = None
		self._cipheader = None
		self._cookieversion = None
		self._securecookie = None
		self._pmtumin = None
		self._pmtutimeout = None
		self._ftpportrange = None
		self._crportrange = None
		self._timezone = None
		self._grantquotamaxclient = None
		self._exclusivequotamaxclient = None
		self._grantquotaspillover = None
		self._exclusivequotaspillover = None
		self._useproxyport = None
		self._internaluserlogin = None
		self._aftpallowrandomsourceport = None
		self._icaports = None
		self._tcpcip = None
		self._servicepathingressvlan = None

	@property
	def httpport(self) :
		r"""HTTP ports on the web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._httpport
		except Exception as e:
			raise e

	@httpport.setter
	def httpport(self, httpport) :
		r"""HTTP ports on the web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._httpport = httpport
		except Exception as e:
			raise e

	@property
	def maxconn(self) :
		r"""Maximum number of connections that will be made from the appliance to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Default value: 0<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxconn
		except Exception as e:
			raise e

	@maxconn.setter
	def maxconn(self, maxconn) :
		r"""Maximum number of connections that will be made from the appliance to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Default value: 0<br/>Maximum length =  4294967294
		"""
		try :
			self._maxconn = maxconn
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""Maximum number of requests that the system can pass on a particular connection between the appliance and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed. This value is overridden by the maximum number of requests configured on the individual service.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""Maximum number of requests that the system can pass on a particular connection between the appliance and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed. This value is overridden by the maximum number of requests configured on the individual service.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Enable or disable the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.
		* If the CIP header is specified, it will be used as the client IP header.
		* If the CIP header is not specified, the value that has been set will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""Enable or disable the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.
		* If the CIP header is specified, it will be used as the client IP header.
		* If the CIP header is not specified, the value that has been set will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""Text that will be used as the client IP address header.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""Text that will be used as the client IP address header.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def cookieversion(self) :
		r"""Version of the cookie inserted by the system.<br/>Possible values = 0, 1.
		"""
		try :
			return self._cookieversion
		except Exception as e:
			raise e

	@cookieversion.setter
	def cookieversion(self, cookieversion) :
		r"""Version of the cookie inserted by the system.<br/>Possible values = 0, 1
		"""
		try :
			self._cookieversion = cookieversion
		except Exception as e:
			raise e

	@property
	def securecookie(self) :
		r"""Enable or disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securecookie
		except Exception as e:
			raise e

	@securecookie.setter
	def securecookie(self, securecookie) :
		r"""Enable or disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securecookie = securecookie
		except Exception as e:
			raise e

	@property
	def pmtumin(self) :
		r"""Minimum path MTU value that NetScaler will process in the ICMP fragmentation needed message. If the ICMP message contains a value less than this value, then this value is used instead.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500.
		"""
		try :
			return self._pmtumin
		except Exception as e:
			raise e

	@pmtumin.setter
	def pmtumin(self, pmtumin) :
		r"""Minimum path MTU value that NetScaler will process in the ICMP fragmentation needed message. If the ICMP message contains a value less than this value, then this value is used instead.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500
		"""
		try :
			self._pmtumin = pmtumin
		except Exception as e:
			raise e

	@property
	def pmtutimeout(self) :
		r"""Interval, in minutes, for flushing the PMTU entries.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._pmtutimeout
		except Exception as e:
			raise e

	@pmtutimeout.setter
	def pmtutimeout(self, pmtutimeout) :
		r"""Interval, in minutes, for flushing the PMTU entries.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._pmtutimeout = pmtutimeout
		except Exception as e:
			raise e

	@property
	def ftpportrange(self) :
		r"""Minimum and maximum port (port range) that FTP services are allowed to use.<br/>Minimum length =  1024<br/>Maximum length =  64000.
		"""
		try :
			return self._ftpportrange
		except Exception as e:
			raise e

	@ftpportrange.setter
	def ftpportrange(self, ftpportrange) :
		r"""Minimum and maximum port (port range) that FTP services are allowed to use.<br/>Minimum length =  1024<br/>Maximum length =  64000
		"""
		try :
			self._ftpportrange = ftpportrange
		except Exception as e:
			raise e

	@property
	def crportrange(self) :
		r"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._crportrange
		except Exception as e:
			raise e

	@crportrange.setter
	def crportrange(self, crportrange) :
		r"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._crportrange = crportrange
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		r"""Time zone for the NetScaler appliance. Name of the time zone should be specified as argument.<br/>Possible values = CoordinatedUniversalTime, GMT+02:00-CEST-Europe/Andorra, GMT+04:00-GST-Asia/Dubai, GMT+04:30-AFT-Asia/Kabul, GMT-04:00-AST-America/Antigua, GMT-04:00-AST-America/Anguilla, GMT+02:00-CEST-Europe/Tirane, GMT+04:00-+04-Asia/Yerevan, GMT+01:00-WAT-Africa/Luanda, GMT+12:00-NZST-Antarctica/McMurdo, GMT+08:00-+08-Antarctica/Casey, GMT+07:00-+07-Antarctica/Davis, GMT+10:00-+10-Antarctica/DumontDUrville, GMT+05:00-+05-Antarctica/Mawson, GMT-03:00-CLST-Antarctica/Palmer, GMT-03:00--03-Antarctica/Rothera, GMT+03:00-+03-Antarctica/Syowa, GMT+02:00-+02-Antarctica/Troll, GMT+06:00-+06-Antarctica/Vostok, GMT-03:00-ART-America/Argentina/Buenos_Aires, GMT-03:00-ART-America/Argentina/Cordoba, GMT-03:00-ART-America/Argentina/Salta, GMT-03:00-ART-America/Argentina/Jujuy, GMT-03:00-ART-America/Argentina/Tucuman, GMT-03:00-ART-America/Argentina/Catamarca, GMT-03:00-ART-America/Argentina/La_Rioja, GMT-03:00-ART-America/Argentina/San_Juan, GMT-03:00-ART-America/Argentina/Mendoza, GMT-03:00-ART-America/Argentina/San_Luis, GMT-03:00-ART-America/Argentina/Rio_Gallegos, GMT-03:00-ART-America/Argentina/Ushuaia, GMT-11:00-SST-Pacific/Pago_Pago, GMT+02:00-CEST-Europe/Vienna, GMT+10:30-LHST-Australia/Lord_Howe, GMT+11:00-MIST-Antarctica/Macquarie, GMT+10:00-AEST-Australia/Hobart, GMT+10:00-AEST-Australia/Currie, GMT+10:00-AEST-Australia/Melbourne, GMT+10:00-AEST-Australia/Sydney, GMT+09:30-ACST-Australia/Broken_Hill, GMT+10:00-AEST-Australia/Brisbane, GMT+10:00-AEST-Australia/Lindeman, GMT+09:30-ACST-Australia/Adelaide, GMT+09:30-ACST-Australia/Darwin, GMT+08:00-AWST-Australia/Perth, GMT+08:45-ACWST-Australia/Eucla, GMT-04:00-AST-America/Aruba, GMT+03:00-EEST-Europe/Mariehamn, GMT+04:00-+04-Asia/Baku, GMT+02:00-CEST-Europe/Sarajevo, GMT-04:00-AST-America/Barbados, GMT+06:00-BDT-Asia/Dhaka, GMT+02:00-CEST-Europe/Brussels, GMT+00:00-GMT-Africa/Ouagadougou, GMT+03:00-EEST-Europe/Sofia, GMT+03:00-AST-Asia/Bahrain, GMT+02:00-CAT-Africa/Bujumbura, GMT+01:00-WAT-Africa/Porto-Novo, GMT-04:00-AST-America/St_Barthelemy, GMT-03:00-ADT-Atlantic/Bermuda, GMT+08:00-BNT-Asia/Brunei, GMT-04:00-BOT-America/La_Paz, GMT-04:00-AST-America/Kralendijk, GMT-02:00-FNT-America/Noronha, GMT-03:00-BRT-America/Belem, GMT-03:00-BRT-America/Fortaleza, GMT-03:00-BRT-America/Recife, GMT-03:00-BRT-America/Araguaina, GMT-03:00-BRT-America/Maceio, GMT-03:00-BRT-America/Bahia, GMT-03:00-BRT-America/Sao_Paulo, GMT-04:00-AMT-America/Campo_Grande, GMT-04:00-AMT-America/Cuiaba, GMT-03:00-BRT-America/Santarem, GMT-04:00-AMT-America/Porto_Velho, GMT-04:00-AMT-America/Boa_Vista, GMT-04:00-AMT-America/Manaus, GMT-05:00-ACT-America/Eirunepe, GMT-05:00-ACT-America/Rio_Branco, GMT-04:00-EDT-America/Nassau, GMT+06:00-BTT-Asia/Thimphu, GMT+02:00-CAT-Africa/Gaborone, GMT+03:00-+03-Europe/Minsk, GMT-06:00-CST-America/Belize, GMT-02:30-NDT-America/St_Johns, GMT-03:00-ADT-America/Halifax, GMT-03:00-ADT-America/Glace_Bay, GMT-03:00-ADT-America/Moncton, GMT-03:00-ADT-America/Goose_Bay, GMT-04:00-AST-America/Blanc-Sablon, GMT-04:00-EDT-America/Toronto, GMT-04:00-EDT-America/Nipigon, GMT-04:00-EDT-America/Thunder_Bay, GMT-04:00-EDT-America/Iqaluit, GMT-04:00-EDT-America/Pangnirtung, GMT-05:00-EST-America/Atikokan, GMT-05:00-CDT-America/Winnipeg, GMT-05:00-CDT-America/Rainy_River, GMT-05:00-CDT-America/Resolute, GMT-05:00-CDT-America/Rankin_Inlet, GMT-06:00-CST-America/Regina, GMT-06:00-CST-America/Swift_Current, GMT-06:00-MDT-America/Edmonton, GMT-06:00-MDT-America/Cambridge_Bay, GMT-06:00-MDT-America/Yellowknife, GMT-06:00-MDT-America/Inuvik, GMT-07:00-MST-America/Creston, GMT-07:00-MST-America/Dawson_Creek, GMT-07:00-MST-America/Fort_Nelson, GMT-07:00-PDT-America/Vancouver, GMT-07:00-PDT-America/Whitehorse, GMT-07:00-PDT-America/Dawson, GMT+06:30-CCT-Indian/Cocos, GMT+01:00-WAT-Africa/Kinshasa, GMT+02:00-CAT-Africa/Lubumbashi, GMT+01:00-WAT-Africa/Bangui, GMT+01:00-WAT-Africa/Brazzaville, GMT+02:00-CEST-Europe/Zurich, GMT+00:00-GMT-Africa/Abidjan, GMT-10:00-CKT-Pacific/Rarotonga, GMT-03:00-CLST-America/Santiago, GMT-05:00-EASST-Pacific/Easter, GMT+01:00-WAT-Africa/Douala, GMT+08:00-CST-Asia/Shanghai, GMT+06:00-XJT-Asia/Urumqi, GMT-05:00-COT-America/Bogota, GMT-06:00-CST-America/Costa_Rica, GMT-04:00-CDT-America/Havana, GMT-01:00-CVT-Atlantic/Cape_Verde, GMT-04:00-AST-America/Curacao, GMT+07:00-CXT-Indian/Christmas, GMT+03:00-EEST-Asia/Nicosia, GMT+02:00-CEST-Europe/Prague, GMT+02:00-CEST-Europe/Berlin, GMT+02:00-CEST-Europe/Busingen, GMT+03:00-EAT-Africa/Djibouti, GMT+02:00-CEST-Europe/Copenhagen, GMT-04:00-AST-America/Dominica, GMT-04:00-AST-America/Santo_Domingo, GMT+01:00-CET-Africa/Algiers, GMT-05:00-ECT-America/Guayaquil, GMT-06:00-GALT-Pacific/Galapagos, GMT+03:00-EEST-Europe/Tallinn, GMT+02:00-EET-Africa/Cairo, GMT+01:00-WEST-Africa/El_Aaiun, GMT+03:00-EAT-Africa/Asmara, GMT+02:00-CEST-Europe/Madrid, GMT+02:00-CEST-Africa/Ceuta, GMT+01:00-WEST-Atlantic/Canary, GMT+03:00-EAT-Africa/Addis_Ababa, GMT+03:00-EEST-Europe/Helsinki, GMT+12:00-FJT-Pacific/Fiji, GMT-03:00-FKST-Atlantic/Stanley, GMT+10:00-CHUT-Pacific/Chuuk, GMT+11:00-PONT-Pacific/Pohnpei, GMT+11:00-KOST-Pacific/Kosrae, GMT+01:00-WEST-Atlantic/Faroe, GMT+02:00-CEST-Europe/Paris, GMT+01:00-WAT-Africa/Libreville, GMT+01:00-BST-Europe/London, GMT-04:00-AST-America/Grenada, GMT+04:00-+04-Asia/Tbilisi, GMT-03:00-GFT-America/Cayenne, GMT+01:00-BST-Europe/Guernsey, GMT+00:00-GMT-Africa/Accra, GMT+02:00-CEST-Europe/Gibraltar, GMT-02:00-WGST-America/Godthab, GMT+00:00-GMT-America/Danmarkshavn, GMT+00:00-EGST-America/Scoresbysund, GMT-03:00-ADT-America/Thule, GMT+00:00-GMT-Africa/Banjul, GMT+00:00-GMT-Africa/Conakry, GMT-04:00-AST-America/Guadeloupe, GMT+01:00-WAT-Africa/Malabo, GMT+03:00-EEST-Europe/Athens, GMT-02:00-GST-Atlantic/South_Georgia, GMT-06:00-CST-America/Guatemala, GMT+10:00-ChST-Pacific/Guam, GMT+00:00-GMT-Africa/Bissau, GMT-04:00-GYT-America/Guyana, GMT+08:00-HKT-Asia/Hong_Kong, GMT-06:00-CST-America/Tegucigalpa, GMT+02:00-CEST-Europe/Zagreb, GMT-05:00-EST-America/Port-au-Prince, GMT+02:00-CEST-Europe/Budapest, GMT+07:00-WIB-Asia/Jakarta, GMT+07:00-WIB-Asia/Pontianak, GMT+08:00-WITA-Asia/Makassar, GMT+09:00-WIT-Asia/Jayapura, GMT+01:00-IST-Europe/Dublin, GMT+03:00-IDT-Asia/Jerusalem, GMT+01:00-BST-Europe/Isle_of_Man, GMT+05:30-IST-Asia/Kolkata, GMT+06:00-IOT-Indian/Chagos, GMT+03:00-AST-Asia/Baghdad, GMT+04:30-IRDT-Asia/Tehran, GMT+00:00-GMT-Atlantic/Reykjavik, GMT+02:00-CEST-Europe/Rome, GMT+01:00-BST-Europe/Jersey, GMT-05:00-EST-America/Jamaica, GMT+03:00-EEST-Asia/Amman, GMT+09:00-JST-Asia/Tokyo, GMT+03:00-EAT-Africa/Nairobi, GMT+06:00-+06-Asia/Bishkek, GMT+07:00-ICT-Asia/Phnom_Penh, GMT+12:00-GILT-Pacific/Tarawa, GMT+13:00-PHOT-Pacific/Enderbury, GMT+14:00-LINT-Pacific/Kiritimati, GMT+03:00-EAT-Indian/Comoro, GMT-04:00-AST-America/St_Kitts, GMT+08:30-KST-Asia/Pyongyang, GMT+09:00-KST-Asia/Seoul, GMT+03:00-AST-Asia/Kuwait, GMT-05:00-EST-America/Cayman, GMT+06:00-+06-Asia/Almaty, GMT+06:00-+06-Asia/Qyzylorda, GMT+05:00-+05-Asia/Aqtobe, GMT+05:00-+05-Asia/Aqtau, GMT+05:00-+05-Asia/Oral, GMT+07:00-ICT-Asia/Vientiane, GMT+03:00-EEST-Asia/Beirut, GMT-04:00-AST-America/St_Lucia, GMT+02:00-CEST-Europe/Vaduz, GMT+05:30-IST-Asia/Colombo, GMT+00:00-GMT-Africa/Monrovia, GMT+02:00-SAST-Africa/Maseru, GMT+03:00-EEST-Europe/Vilnius, GMT+02:00-CEST-Europe/Luxembourg, GMT+03:00-EEST-Europe/Riga, GMT+02:00-EET-Africa/Tripoli, GMT+01:00-WEST-Africa/Casablanca, GMT+02:00-CEST-Europe/Monaco, GMT+03:00-EEST-Europe/Chisinau, GMT+02:00-CEST-Europe/Podgorica, GMT-04:00-AST-America/Marigot, GMT+03:00-EAT-Indian/Antananarivo, GMT+12:00-MHT-Pacific/Majuro, GMT+12:00-MHT-Pacific/Kwajalein, GMT+02:00-CEST-Europe/Skopje, GMT+00:00-GMT-Africa/Bamako, GMT+06:30-MMT-Asia/Yangon, GMT+09:00-ULAST-Asia/Ulaanbaatar, GMT+08:00-HOVST-Asia/Hovd, GMT+09:00-CHOST-Asia/Choibalsan, GMT+08:00-CST-Asia/Macau, GMT+10:00-ChST-Pacific/Saipan, GMT-04:00-AST-America/Martinique, GMT+00:00-GMT-Africa/Nouakchott, GMT-04:00-AST-America/Montserrat, GMT+02:00-CEST-Europe/Malta, GMT+04:00-MUT-Indian/Mauritius, GMT+05:00-MVT-Indian/Maldives, GMT+02:00-CAT-Africa/Blantyre, GMT-05:00-CDT-America/Mexico_City, GMT-05:00-EST-America/Cancun, GMT-05:00-CDT-America/Merida, GMT-05:00-CDT-America/Monterrey, GMT-05:00-CDT-America/Matamoros, GMT-06:00-MDT-America/Mazatlan, GMT-06:00-MDT-America/Chihuahua, GMT-06:00-MDT-America/Ojinaga, GMT-07:00-MST-America/Hermosillo, GMT-07:00-PDT-America/Tijuana, GMT-05:00-CDT-America/Bahia_Banderas, GMT+08:00-MYT-Asia/Kuala_Lumpur, GMT+08:00-MYT-Asia/Kuching, GMT+02:00-CAT-Africa/Maputo, GMT+01:00-WAT-Africa/Windhoek, GMT+11:00-NCT-Pacific/Noumea, GMT+01:00-WAT-Africa/Niamey, GMT+11:00-NFT-Pacific/Norfolk, GMT+01:00-WAT-Africa/Lagos, GMT-06:00-CST-America/Managua, GMT+02:00-CEST-Europe/Amsterdam, GMT+02:00-CEST-Europe/Oslo, GMT+05:45-NPT-Asia/Kathmandu, GMT+12:00-NRT-Pacific/Nauru, GMT-11:00-NUT-Pacific/Niue, GMT+12:00-NZST-Pacific/Auckland, GMT+12:45-CHAST-Pacific/Chatham, GMT+04:00-GST-Asia/Muscat, GMT-05:00-EST-America/Panama, GMT-05:00-PET-America/Lima, GMT-10:00-TAHT-Pacific/Tahiti, GMT-09:30-MART-Pacific/Marquesas, GMT-09:00-GAMT-Pacific/Gambier, GMT+10:00-PGT-Pacific/Port_Moresby, GMT+11:00-BST-Pacific/Bougainville, GMT+08:00-PHT-Asia/Manila, GMT+05:00-PKT-Asia/Karachi, GMT+02:00-CEST-Europe/Warsaw, GMT-02:00-PMDT-America/Miquelon, GMT-08:00-PST-Pacific/Pitcairn, GMT-04:00-AST-America/Puerto_Rico, GMT+03:00-EEST-Asia/Gaza, GMT+03:00-EEST-Asia/Hebron, GMT+01:00-WEST-Europe/Lisbon, GMT+01:00-WEST-Atlantic/Madeira, GMT+00:00-AZOST-Atlantic/Azores, GMT+09:00-PWT-Pacific/Palau, GMT-04:00-PYT-America/Asuncion, GMT+03:00-AST-Asia/Qatar, GMT+04:00-RET-Indian/Reunion, GMT+03:00-EEST-Europe/Bucharest, GMT+02:00-CEST-Europe/Belgrade, GMT+02:00-EET-Europe/Kaliningrad, GMT+03:00-MSK-Europe/Moscow, GMT+03:00-MSK-Europe/Simferopol, GMT+03:00-+03-Europe/Volgograd, GMT+03:00-+03-Europe/Kirov, GMT+04:00-+04-Europe/Astrakhan, GMT+04:00-+04-Europe/Samara, GMT+04:00-+04-Europe/Ulyanovsk, GMT+05:00-+05-Asia/Yekaterinburg, GMT+06:00-+06-Asia/Omsk, GMT+07:00-+07-Asia/Novosibirsk, GMT+07:00-+07-Asia/Barnaul, GMT+07:00-+07-Asia/Tomsk, GMT+07:00-+07-Asia/Novokuznetsk, GMT+07:00-+07-Asia/Krasnoyarsk, GMT+08:00-+08-Asia/Irkutsk, GMT+09:00-+09-Asia/Chita, GMT+09:00-+09-Asia/Yakutsk, GMT+09:00-+09-Asia/Khandyga, GMT+10:00-+10-Asia/Vladivostok, GMT+10:00-+10-Asia/Ust-Nera, GMT+11:00-+11-Asia/Magadan, GMT+11:00-+11-Asia/Sakhalin, GMT+11:00-+11-Asia/Srednekolymsk, GMT+12:00-+12-Asia/Kamchatka, GMT+12:00-+12-Asia/Anadyr, GMT+02:00-CAT-Africa/Kigali, GMT+03:00-AST-Asia/Riyadh, GMT+11:00-SBT-Pacific/Guadalcanal, GMT+04:00-SCT-Indian/Mahe, GMT+03:00-EAT-Africa/Khartoum, GMT+02:00-CEST-Europe/Stockholm, GMT+08:00-SGT-Asia/Singapore, GMT+00:00-GMT-Atlantic/St_Helena, GMT+02:00-CEST-Europe/Ljubljana, GMT+02:00-CEST-Arctic/Longyearbyen, GMT+02:00-CEST-Europe/Bratislava, GMT+00:00-GMT-Africa/Freetown, GMT+02:00-CEST-Europe/San_Marino, GMT+00:00-GMT-Africa/Dakar, GMT+03:00-EAT-Africa/Mogadishu, GMT-03:00-SRT-America/Paramaribo, GMT+03:00-EAT-Africa/Juba, GMT+00:00-GMT-Africa/Sao_Tome, GMT-06:00-CST-America/El_Salvador, GMT-04:00-AST-America/Lower_Princes, GMT+03:00-EEST-Asia/Damascus, GMT+02:00-SAST-Africa/Mbabane, GMT-04:00-AST-America/Grand_Turk, GMT+01:00-WAT-Africa/Ndjamena, GMT+05:00-+05-Indian/Kerguelen, GMT+00:00-GMT-Africa/Lome, GMT+07:00-ICT-Asia/Bangkok, GMT+05:00-+05-Asia/Dushanbe, GMT+13:00-TKT-Pacific/Fakaofo, GMT+09:00-TLT-Asia/Dili, GMT+05:00-+05-Asia/Ashgabat, GMT+01:00-CET-Africa/Tunis, GMT+13:00-TOT-Pacific/Tongatapu, GMT+03:00-+03-Europe/Istanbul, GMT-04:00-AST-America/Port_of_Spain, GMT+12:00-TVT-Pacific/Funafuti, GMT+08:00-CST-Asia/Taipei, GMT+03:00-EAT-Africa/Dar_es_Salaam, GMT+03:00-EEST-Europe/Kiev, GMT+03:00-EEST-Europe/Uzhgorod, GMT+03:00-EEST-Europe/Zaporozhye, GMT+03:00-EAT-Africa/Kampala, GMT-10:00-HST-Pacific/Johnston, GMT-11:00-SST-Pacific/Midway, GMT+12:00-WAKT-Pacific/Wake, GMT-04:00-EDT-America/New_York, GMT-04:00-EDT-America/Detroit, GMT-04:00-EDT-America/Kentucky/Louisville, GMT-04:00-EDT-America/Kentucky/Monticello, GMT-04:00-EDT-America/Indiana/Indianapolis, GMT-04:00-EDT-America/Indiana/Vincennes, GMT-04:00-EDT-America/Indiana/Winamac, GMT-04:00-EDT-America/Indiana/Marengo, GMT-04:00-EDT-America/Indiana/Petersburg, GMT-04:00-EDT-America/Indiana/Vevay, GMT-05:00-CDT-America/Chicago, GMT-05:00-CDT-America/Indiana/Tell_City, GMT-05:00-CDT-America/Indiana/Knox, GMT-05:00-CDT-America/Menominee, GMT-05:00-CDT-America/North_Dakota/Center, GMT-05:00-CDT-America/North_Dakota/New_Salem, GMT-05:00-CDT-America/North_Dakota/Beulah, GMT-06:00-MDT-America/Denver, GMT-06:00-MDT-America/Boise, GMT-07:00-MST-America/Phoenix, GMT-07:00-PDT-America/Los_Angeles, GMT-08:00-AKDT-America/Anchorage, GMT-08:00-AKDT-America/Juneau, GMT-08:00-AKDT-America/Sitka, GMT-08:00-AKDT-America/Metlakatla, GMT-08:00-AKDT-America/Yakutat, GMT-08:00-AKDT-America/Nome, GMT-09:00-HDT-America/Adak, GMT-10:00-HST-Pacific/Honolulu, GMT-03:00-UYT-America/Montevideo, GMT+05:00-+05-Asia/Samarkand, GMT+05:00-+05-Asia/Tashkent, GMT+02:00-CEST-Europe/Vatican, GMT-04:00-AST-America/St_Vincent, GMT-04:00-VET-America/Caracas, GMT-04:00-AST-America/Tortola, GMT-04:00-AST-America/St_Thomas, GMT+07:00-ICT-Asia/Ho_Chi_Minh, GMT+11:00-VUT-Pacific/Efate, GMT+12:00-WFT-Pacific/Wallis, GMT+13:00-WSST-Pacific/Apia, GMT+03:00-AST-Asia/Aden, GMT+03:00-EAT-Indian/Mayotte, GMT+02:00-SAST-Africa/Johannesburg, GMT+02:00-CAT-Africa/Lusaka, GMT+02:00-CAT-Africa/Harare.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		r"""Time zone for the NetScaler appliance. Name of the time zone should be specified as argument.<br/>Possible values = CoordinatedUniversalTime, GMT+02:00-CEST-Europe/Andorra, GMT+04:00-GST-Asia/Dubai, GMT+04:30-AFT-Asia/Kabul, GMT-04:00-AST-America/Antigua, GMT-04:00-AST-America/Anguilla, GMT+02:00-CEST-Europe/Tirane, GMT+04:00-+04-Asia/Yerevan, GMT+01:00-WAT-Africa/Luanda, GMT+12:00-NZST-Antarctica/McMurdo, GMT+08:00-+08-Antarctica/Casey, GMT+07:00-+07-Antarctica/Davis, GMT+10:00-+10-Antarctica/DumontDUrville, GMT+05:00-+05-Antarctica/Mawson, GMT-03:00-CLST-Antarctica/Palmer, GMT-03:00--03-Antarctica/Rothera, GMT+03:00-+03-Antarctica/Syowa, GMT+02:00-+02-Antarctica/Troll, GMT+06:00-+06-Antarctica/Vostok, GMT-03:00-ART-America/Argentina/Buenos_Aires, GMT-03:00-ART-America/Argentina/Cordoba, GMT-03:00-ART-America/Argentina/Salta, GMT-03:00-ART-America/Argentina/Jujuy, GMT-03:00-ART-America/Argentina/Tucuman, GMT-03:00-ART-America/Argentina/Catamarca, GMT-03:00-ART-America/Argentina/La_Rioja, GMT-03:00-ART-America/Argentina/San_Juan, GMT-03:00-ART-America/Argentina/Mendoza, GMT-03:00-ART-America/Argentina/San_Luis, GMT-03:00-ART-America/Argentina/Rio_Gallegos, GMT-03:00-ART-America/Argentina/Ushuaia, GMT-11:00-SST-Pacific/Pago_Pago, GMT+02:00-CEST-Europe/Vienna, GMT+10:30-LHST-Australia/Lord_Howe, GMT+11:00-MIST-Antarctica/Macquarie, GMT+10:00-AEST-Australia/Hobart, GMT+10:00-AEST-Australia/Currie, GMT+10:00-AEST-Australia/Melbourne, GMT+10:00-AEST-Australia/Sydney, GMT+09:30-ACST-Australia/Broken_Hill, GMT+10:00-AEST-Australia/Brisbane, GMT+10:00-AEST-Australia/Lindeman, GMT+09:30-ACST-Australia/Adelaide, GMT+09:30-ACST-Australia/Darwin, GMT+08:00-AWST-Australia/Perth, GMT+08:45-ACWST-Australia/Eucla, GMT-04:00-AST-America/Aruba, GMT+03:00-EEST-Europe/Mariehamn, GMT+04:00-+04-Asia/Baku, GMT+02:00-CEST-Europe/Sarajevo, GMT-04:00-AST-America/Barbados, GMT+06:00-BDT-Asia/Dhaka, GMT+02:00-CEST-Europe/Brussels, GMT+00:00-GMT-Africa/Ouagadougou, GMT+03:00-EEST-Europe/Sofia, GMT+03:00-AST-Asia/Bahrain, GMT+02:00-CAT-Africa/Bujumbura, GMT+01:00-WAT-Africa/Porto-Novo, GMT-04:00-AST-America/St_Barthelemy, GMT-03:00-ADT-Atlantic/Bermuda, GMT+08:00-BNT-Asia/Brunei, GMT-04:00-BOT-America/La_Paz, GMT-04:00-AST-America/Kralendijk, GMT-02:00-FNT-America/Noronha, GMT-03:00-BRT-America/Belem, GMT-03:00-BRT-America/Fortaleza, GMT-03:00-BRT-America/Recife, GMT-03:00-BRT-America/Araguaina, GMT-03:00-BRT-America/Maceio, GMT-03:00-BRT-America/Bahia, GMT-03:00-BRT-America/Sao_Paulo, GMT-04:00-AMT-America/Campo_Grande, GMT-04:00-AMT-America/Cuiaba, GMT-03:00-BRT-America/Santarem, GMT-04:00-AMT-America/Porto_Velho, GMT-04:00-AMT-America/Boa_Vista, GMT-04:00-AMT-America/Manaus, GMT-05:00-ACT-America/Eirunepe, GMT-05:00-ACT-America/Rio_Branco, GMT-04:00-EDT-America/Nassau, GMT+06:00-BTT-Asia/Thimphu, GMT+02:00-CAT-Africa/Gaborone, GMT+03:00-+03-Europe/Minsk, GMT-06:00-CST-America/Belize, GMT-02:30-NDT-America/St_Johns, GMT-03:00-ADT-America/Halifax, GMT-03:00-ADT-America/Glace_Bay, GMT-03:00-ADT-America/Moncton, GMT-03:00-ADT-America/Goose_Bay, GMT-04:00-AST-America/Blanc-Sablon, GMT-04:00-EDT-America/Toronto, GMT-04:00-EDT-America/Nipigon, GMT-04:00-EDT-America/Thunder_Bay, GMT-04:00-EDT-America/Iqaluit, GMT-04:00-EDT-America/Pangnirtung, GMT-05:00-EST-America/Atikokan, GMT-05:00-CDT-America/Winnipeg, GMT-05:00-CDT-America/Rainy_River, GMT-05:00-CDT-America/Resolute, GMT-05:00-CDT-America/Rankin_Inlet, GMT-06:00-CST-America/Regina, GMT-06:00-CST-America/Swift_Current, GMT-06:00-MDT-America/Edmonton, GMT-06:00-MDT-America/Cambridge_Bay, GMT-06:00-MDT-America/Yellowknife, GMT-06:00-MDT-America/Inuvik, GMT-07:00-MST-America/Creston, GMT-07:00-MST-America/Dawson_Creek, GMT-07:00-MST-America/Fort_Nelson, GMT-07:00-PDT-America/Vancouver, GMT-07:00-PDT-America/Whitehorse, GMT-07:00-PDT-America/Dawson, GMT+06:30-CCT-Indian/Cocos, GMT+01:00-WAT-Africa/Kinshasa, GMT+02:00-CAT-Africa/Lubumbashi, GMT+01:00-WAT-Africa/Bangui, GMT+01:00-WAT-Africa/Brazzaville, GMT+02:00-CEST-Europe/Zurich, GMT+00:00-GMT-Africa/Abidjan, GMT-10:00-CKT-Pacific/Rarotonga, GMT-03:00-CLST-America/Santiago, GMT-05:00-EASST-Pacific/Easter, GMT+01:00-WAT-Africa/Douala, GMT+08:00-CST-Asia/Shanghai, GMT+06:00-XJT-Asia/Urumqi, GMT-05:00-COT-America/Bogota, GMT-06:00-CST-America/Costa_Rica, GMT-04:00-CDT-America/Havana, GMT-01:00-CVT-Atlantic/Cape_Verde, GMT-04:00-AST-America/Curacao, GMT+07:00-CXT-Indian/Christmas, GMT+03:00-EEST-Asia/Nicosia, GMT+02:00-CEST-Europe/Prague, GMT+02:00-CEST-Europe/Berlin, GMT+02:00-CEST-Europe/Busingen, GMT+03:00-EAT-Africa/Djibouti, GMT+02:00-CEST-Europe/Copenhagen, GMT-04:00-AST-America/Dominica, GMT-04:00-AST-America/Santo_Domingo, GMT+01:00-CET-Africa/Algiers, GMT-05:00-ECT-America/Guayaquil, GMT-06:00-GALT-Pacific/Galapagos, GMT+03:00-EEST-Europe/Tallinn, GMT+02:00-EET-Africa/Cairo, GMT+01:00-WEST-Africa/El_Aaiun, GMT+03:00-EAT-Africa/Asmara, GMT+02:00-CEST-Europe/Madrid, GMT+02:00-CEST-Africa/Ceuta, GMT+01:00-WEST-Atlantic/Canary, GMT+03:00-EAT-Africa/Addis_Ababa, GMT+03:00-EEST-Europe/Helsinki, GMT+12:00-FJT-Pacific/Fiji, GMT-03:00-FKST-Atlantic/Stanley, GMT+10:00-CHUT-Pacific/Chuuk, GMT+11:00-PONT-Pacific/Pohnpei, GMT+11:00-KOST-Pacific/Kosrae, GMT+01:00-WEST-Atlantic/Faroe, GMT+02:00-CEST-Europe/Paris, GMT+01:00-WAT-Africa/Libreville, GMT+01:00-BST-Europe/London, GMT-04:00-AST-America/Grenada, GMT+04:00-+04-Asia/Tbilisi, GMT-03:00-GFT-America/Cayenne, GMT+01:00-BST-Europe/Guernsey, GMT+00:00-GMT-Africa/Accra, GMT+02:00-CEST-Europe/Gibraltar, GMT-02:00-WGST-America/Godthab, GMT+00:00-GMT-America/Danmarkshavn, GMT+00:00-EGST-America/Scoresbysund, GMT-03:00-ADT-America/Thule, GMT+00:00-GMT-Africa/Banjul, GMT+00:00-GMT-Africa/Conakry, GMT-04:00-AST-America/Guadeloupe, GMT+01:00-WAT-Africa/Malabo, GMT+03:00-EEST-Europe/Athens, GMT-02:00-GST-Atlantic/South_Georgia, GMT-06:00-CST-America/Guatemala, GMT+10:00-ChST-Pacific/Guam, GMT+00:00-GMT-Africa/Bissau, GMT-04:00-GYT-America/Guyana, GMT+08:00-HKT-Asia/Hong_Kong, GMT-06:00-CST-America/Tegucigalpa, GMT+02:00-CEST-Europe/Zagreb, GMT-05:00-EST-America/Port-au-Prince, GMT+02:00-CEST-Europe/Budapest, GMT+07:00-WIB-Asia/Jakarta, GMT+07:00-WIB-Asia/Pontianak, GMT+08:00-WITA-Asia/Makassar, GMT+09:00-WIT-Asia/Jayapura, GMT+01:00-IST-Europe/Dublin, GMT+03:00-IDT-Asia/Jerusalem, GMT+01:00-BST-Europe/Isle_of_Man, GMT+05:30-IST-Asia/Kolkata, GMT+06:00-IOT-Indian/Chagos, GMT+03:00-AST-Asia/Baghdad, GMT+04:30-IRDT-Asia/Tehran, GMT+00:00-GMT-Atlantic/Reykjavik, GMT+02:00-CEST-Europe/Rome, GMT+01:00-BST-Europe/Jersey, GMT-05:00-EST-America/Jamaica, GMT+03:00-EEST-Asia/Amman, GMT+09:00-JST-Asia/Tokyo, GMT+03:00-EAT-Africa/Nairobi, GMT+06:00-+06-Asia/Bishkek, GMT+07:00-ICT-Asia/Phnom_Penh, GMT+12:00-GILT-Pacific/Tarawa, GMT+13:00-PHOT-Pacific/Enderbury, GMT+14:00-LINT-Pacific/Kiritimati, GMT+03:00-EAT-Indian/Comoro, GMT-04:00-AST-America/St_Kitts, GMT+08:30-KST-Asia/Pyongyang, GMT+09:00-KST-Asia/Seoul, GMT+03:00-AST-Asia/Kuwait, GMT-05:00-EST-America/Cayman, GMT+06:00-+06-Asia/Almaty, GMT+06:00-+06-Asia/Qyzylorda, GMT+05:00-+05-Asia/Aqtobe, GMT+05:00-+05-Asia/Aqtau, GMT+05:00-+05-Asia/Oral, GMT+07:00-ICT-Asia/Vientiane, GMT+03:00-EEST-Asia/Beirut, GMT-04:00-AST-America/St_Lucia, GMT+02:00-CEST-Europe/Vaduz, GMT+05:30-IST-Asia/Colombo, GMT+00:00-GMT-Africa/Monrovia, GMT+02:00-SAST-Africa/Maseru, GMT+03:00-EEST-Europe/Vilnius, GMT+02:00-CEST-Europe/Luxembourg, GMT+03:00-EEST-Europe/Riga, GMT+02:00-EET-Africa/Tripoli, GMT+01:00-WEST-Africa/Casablanca, GMT+02:00-CEST-Europe/Monaco, GMT+03:00-EEST-Europe/Chisinau, GMT+02:00-CEST-Europe/Podgorica, GMT-04:00-AST-America/Marigot, GMT+03:00-EAT-Indian/Antananarivo, GMT+12:00-MHT-Pacific/Majuro, GMT+12:00-MHT-Pacific/Kwajalein, GMT+02:00-CEST-Europe/Skopje, GMT+00:00-GMT-Africa/Bamako, GMT+06:30-MMT-Asia/Yangon, GMT+09:00-ULAST-Asia/Ulaanbaatar, GMT+08:00-HOVST-Asia/Hovd, GMT+09:00-CHOST-Asia/Choibalsan, GMT+08:00-CST-Asia/Macau, GMT+10:00-ChST-Pacific/Saipan, GMT-04:00-AST-America/Martinique, GMT+00:00-GMT-Africa/Nouakchott, GMT-04:00-AST-America/Montserrat, GMT+02:00-CEST-Europe/Malta, GMT+04:00-MUT-Indian/Mauritius, GMT+05:00-MVT-Indian/Maldives, GMT+02:00-CAT-Africa/Blantyre, GMT-05:00-CDT-America/Mexico_City, GMT-05:00-EST-America/Cancun, GMT-05:00-CDT-America/Merida, GMT-05:00-CDT-America/Monterrey, GMT-05:00-CDT-America/Matamoros, GMT-06:00-MDT-America/Mazatlan, GMT-06:00-MDT-America/Chihuahua, GMT-06:00-MDT-America/Ojinaga, GMT-07:00-MST-America/Hermosillo, GMT-07:00-PDT-America/Tijuana, GMT-05:00-CDT-America/Bahia_Banderas, GMT+08:00-MYT-Asia/Kuala_Lumpur, GMT+08:00-MYT-Asia/Kuching, GMT+02:00-CAT-Africa/Maputo, GMT+01:00-WAT-Africa/Windhoek, GMT+11:00-NCT-Pacific/Noumea, GMT+01:00-WAT-Africa/Niamey, GMT+11:00-NFT-Pacific/Norfolk, GMT+01:00-WAT-Africa/Lagos, GMT-06:00-CST-America/Managua, GMT+02:00-CEST-Europe/Amsterdam, GMT+02:00-CEST-Europe/Oslo, GMT+05:45-NPT-Asia/Kathmandu, GMT+12:00-NRT-Pacific/Nauru, GMT-11:00-NUT-Pacific/Niue, GMT+12:00-NZST-Pacific/Auckland, GMT+12:45-CHAST-Pacific/Chatham, GMT+04:00-GST-Asia/Muscat, GMT-05:00-EST-America/Panama, GMT-05:00-PET-America/Lima, GMT-10:00-TAHT-Pacific/Tahiti, GMT-09:30-MART-Pacific/Marquesas, GMT-09:00-GAMT-Pacific/Gambier, GMT+10:00-PGT-Pacific/Port_Moresby, GMT+11:00-BST-Pacific/Bougainville, GMT+08:00-PHT-Asia/Manila, GMT+05:00-PKT-Asia/Karachi, GMT+02:00-CEST-Europe/Warsaw, GMT-02:00-PMDT-America/Miquelon, GMT-08:00-PST-Pacific/Pitcairn, GMT-04:00-AST-America/Puerto_Rico, GMT+03:00-EEST-Asia/Gaza, GMT+03:00-EEST-Asia/Hebron, GMT+01:00-WEST-Europe/Lisbon, GMT+01:00-WEST-Atlantic/Madeira, GMT+00:00-AZOST-Atlantic/Azores, GMT+09:00-PWT-Pacific/Palau, GMT-04:00-PYT-America/Asuncion, GMT+03:00-AST-Asia/Qatar, GMT+04:00-RET-Indian/Reunion, GMT+03:00-EEST-Europe/Bucharest, GMT+02:00-CEST-Europe/Belgrade, GMT+02:00-EET-Europe/Kaliningrad, GMT+03:00-MSK-Europe/Moscow, GMT+03:00-MSK-Europe/Simferopol, GMT+03:00-+03-Europe/Volgograd, GMT+03:00-+03-Europe/Kirov, GMT+04:00-+04-Europe/Astrakhan, GMT+04:00-+04-Europe/Samara, GMT+04:00-+04-Europe/Ulyanovsk, GMT+05:00-+05-Asia/Yekaterinburg, GMT+06:00-+06-Asia/Omsk, GMT+07:00-+07-Asia/Novosibirsk, GMT+07:00-+07-Asia/Barnaul, GMT+07:00-+07-Asia/Tomsk, GMT+07:00-+07-Asia/Novokuznetsk, GMT+07:00-+07-Asia/Krasnoyarsk, GMT+08:00-+08-Asia/Irkutsk, GMT+09:00-+09-Asia/Chita, GMT+09:00-+09-Asia/Yakutsk, GMT+09:00-+09-Asia/Khandyga, GMT+10:00-+10-Asia/Vladivostok, GMT+10:00-+10-Asia/Ust-Nera, GMT+11:00-+11-Asia/Magadan, GMT+11:00-+11-Asia/Sakhalin, GMT+11:00-+11-Asia/Srednekolymsk, GMT+12:00-+12-Asia/Kamchatka, GMT+12:00-+12-Asia/Anadyr, GMT+02:00-CAT-Africa/Kigali, GMT+03:00-AST-Asia/Riyadh, GMT+11:00-SBT-Pacific/Guadalcanal, GMT+04:00-SCT-Indian/Mahe, GMT+03:00-EAT-Africa/Khartoum, GMT+02:00-CEST-Europe/Stockholm, GMT+08:00-SGT-Asia/Singapore, GMT+00:00-GMT-Atlantic/St_Helena, GMT+02:00-CEST-Europe/Ljubljana, GMT+02:00-CEST-Arctic/Longyearbyen, GMT+02:00-CEST-Europe/Bratislava, GMT+00:00-GMT-Africa/Freetown, GMT+02:00-CEST-Europe/San_Marino, GMT+00:00-GMT-Africa/Dakar, GMT+03:00-EAT-Africa/Mogadishu, GMT-03:00-SRT-America/Paramaribo, GMT+03:00-EAT-Africa/Juba, GMT+00:00-GMT-Africa/Sao_Tome, GMT-06:00-CST-America/El_Salvador, GMT-04:00-AST-America/Lower_Princes, GMT+03:00-EEST-Asia/Damascus, GMT+02:00-SAST-Africa/Mbabane, GMT-04:00-AST-America/Grand_Turk, GMT+01:00-WAT-Africa/Ndjamena, GMT+05:00-+05-Indian/Kerguelen, GMT+00:00-GMT-Africa/Lome, GMT+07:00-ICT-Asia/Bangkok, GMT+05:00-+05-Asia/Dushanbe, GMT+13:00-TKT-Pacific/Fakaofo, GMT+09:00-TLT-Asia/Dili, GMT+05:00-+05-Asia/Ashgabat, GMT+01:00-CET-Africa/Tunis, GMT+13:00-TOT-Pacific/Tongatapu, GMT+03:00-+03-Europe/Istanbul, GMT-04:00-AST-America/Port_of_Spain, GMT+12:00-TVT-Pacific/Funafuti, GMT+08:00-CST-Asia/Taipei, GMT+03:00-EAT-Africa/Dar_es_Salaam, GMT+03:00-EEST-Europe/Kiev, GMT+03:00-EEST-Europe/Uzhgorod, GMT+03:00-EEST-Europe/Zaporozhye, GMT+03:00-EAT-Africa/Kampala, GMT-10:00-HST-Pacific/Johnston, GMT-11:00-SST-Pacific/Midway, GMT+12:00-WAKT-Pacific/Wake, GMT-04:00-EDT-America/New_York, GMT-04:00-EDT-America/Detroit, GMT-04:00-EDT-America/Kentucky/Louisville, GMT-04:00-EDT-America/Kentucky/Monticello, GMT-04:00-EDT-America/Indiana/Indianapolis, GMT-04:00-EDT-America/Indiana/Vincennes, GMT-04:00-EDT-America/Indiana/Winamac, GMT-04:00-EDT-America/Indiana/Marengo, GMT-04:00-EDT-America/Indiana/Petersburg, GMT-04:00-EDT-America/Indiana/Vevay, GMT-05:00-CDT-America/Chicago, GMT-05:00-CDT-America/Indiana/Tell_City, GMT-05:00-CDT-America/Indiana/Knox, GMT-05:00-CDT-America/Menominee, GMT-05:00-CDT-America/North_Dakota/Center, GMT-05:00-CDT-America/North_Dakota/New_Salem, GMT-05:00-CDT-America/North_Dakota/Beulah, GMT-06:00-MDT-America/Denver, GMT-06:00-MDT-America/Boise, GMT-07:00-MST-America/Phoenix, GMT-07:00-PDT-America/Los_Angeles, GMT-08:00-AKDT-America/Anchorage, GMT-08:00-AKDT-America/Juneau, GMT-08:00-AKDT-America/Sitka, GMT-08:00-AKDT-America/Metlakatla, GMT-08:00-AKDT-America/Yakutat, GMT-08:00-AKDT-America/Nome, GMT-09:00-HDT-America/Adak, GMT-10:00-HST-Pacific/Honolulu, GMT-03:00-UYT-America/Montevideo, GMT+05:00-+05-Asia/Samarkand, GMT+05:00-+05-Asia/Tashkent, GMT+02:00-CEST-Europe/Vatican, GMT-04:00-AST-America/St_Vincent, GMT-04:00-VET-America/Caracas, GMT-04:00-AST-America/Tortola, GMT-04:00-AST-America/St_Thomas, GMT+07:00-ICT-Asia/Ho_Chi_Minh, GMT+11:00-VUT-Pacific/Efate, GMT+12:00-WFT-Pacific/Wallis, GMT+13:00-WSST-Pacific/Apia, GMT+03:00-AST-Asia/Aden, GMT+03:00-EAT-Indian/Mayotte, GMT+02:00-SAST-Africa/Johannesburg, GMT+02:00-CAT-Africa/Lusaka, GMT+02:00-CAT-Africa/Harare
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def grantquotamaxclient(self) :
		r"""Percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotamaxclient
		except Exception as e:
			raise e

	@grantquotamaxclient.setter
	def grantquotamaxclient(self, grantquotamaxclient) :
		r"""Percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotamaxclient = grantquotamaxclient
		except Exception as e:
			raise e

	@property
	def exclusivequotamaxclient(self) :
		r"""Percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotamaxclient
		except Exception as e:
			raise e

	@exclusivequotamaxclient.setter
	def exclusivequotamaxclient(self, exclusivequotamaxclient) :
		r"""Percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotamaxclient = exclusivequotamaxclient
		except Exception as e:
			raise e

	@property
	def grantquotaspillover(self) :
		r"""Percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotaspillover
		except Exception as e:
			raise e

	@grantquotaspillover.setter
	def grantquotaspillover(self, grantquotaspillover) :
		r"""Percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotaspillover = grantquotaspillover
		except Exception as e:
			raise e

	@property
	def exclusivequotaspillover(self) :
		r"""Percentage of maximum limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotaspillover
		except Exception as e:
			raise e

	@exclusivequotaspillover.setter
	def exclusivequotaspillover(self, exclusivequotaspillover) :
		r"""Percentage of maximum limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotaspillover = exclusivequotaspillover
		except Exception as e:
			raise e

	@property
	def useproxyport(self) :
		r"""Enable/Disable use_proxy_port setting.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._useproxyport
		except Exception as e:
			raise e

	@useproxyport.setter
	def useproxyport(self, useproxyport) :
		r"""Enable/Disable use_proxy_port setting.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._useproxyport = useproxyport
		except Exception as e:
			raise e

	@property
	def internaluserlogin(self) :
		r"""Enables/disables the internal user from logging in to the appliance. Before disabling internal user login, you must have key-based authentication set up on the appliance. The file name for the key pair must be "ns_comm_key".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._internaluserlogin
		except Exception as e:
			raise e

	@internaluserlogin.setter
	def internaluserlogin(self, internaluserlogin) :
		r"""Enables/disables the internal user from logging in to the appliance. Before disabling internal user login, you must have key-based authentication set up on the appliance. The file name for the key pair must be "ns_comm_key".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._internaluserlogin = internaluserlogin
		except Exception as e:
			raise e

	@property
	def aftpallowrandomsourceport(self) :
		r"""Allow the FTP server to come from a random source port for active FTP data connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._aftpallowrandomsourceport
		except Exception as e:
			raise e

	@aftpallowrandomsourceport.setter
	def aftpallowrandomsourceport(self, aftpallowrandomsourceport) :
		r"""Allow the FTP server to come from a random source port for active FTP data connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._aftpallowrandomsourceport = aftpallowrandomsourceport
		except Exception as e:
			raise e

	@property
	def icaports(self) :
		r"""The ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1.
		"""
		try :
			return self._icaports
		except Exception as e:
			raise e

	@icaports.setter
	def icaports(self, icaports) :
		r"""The ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1
		"""
		try :
			self._icaports = icaports
		except Exception as e:
			raise e

	@property
	def tcpcip(self) :
		r"""Enable or disable the insertion of the client TCP/IP header in TCP payload passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpcip
		except Exception as e:
			raise e

	@tcpcip.setter
	def tcpcip(self, tcpcip) :
		r"""Enable or disable the insertion of the client TCP/IP header in TCP payload passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpcip = tcpcip
		except Exception as e:
			raise e

	@property
	def servicepathingressvlan(self) :
		r"""VLAN on which the subscriber traffic arrives on the appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathingressvlan
		except Exception as e:
			raise e

	@servicepathingressvlan.setter
	def servicepathingressvlan(self, servicepathingressvlan) :
		r"""VLAN on which the subscriber traffic arrives on the appliance.<br/>Minimum length =  1
		"""
		try :
			self._servicepathingressvlan = servicepathingressvlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsparam
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsparam()
				updateresource.httpport = resource.httpport
				updateresource.maxconn = resource.maxconn
				updateresource.maxreq = resource.maxreq
				updateresource.cip = resource.cip
				updateresource.cipheader = resource.cipheader
				updateresource.cookieversion = resource.cookieversion
				updateresource.securecookie = resource.securecookie
				updateresource.pmtumin = resource.pmtumin
				updateresource.pmtutimeout = resource.pmtutimeout
				updateresource.ftpportrange = resource.ftpportrange
				updateresource.crportrange = resource.crportrange
				updateresource.timezone = resource.timezone
				updateresource.grantquotamaxclient = resource.grantquotamaxclient
				updateresource.exclusivequotamaxclient = resource.exclusivequotamaxclient
				updateresource.grantquotaspillover = resource.grantquotaspillover
				updateresource.exclusivequotaspillover = resource.exclusivequotaspillover
				updateresource.useproxyport = resource.useproxyport
				updateresource.internaluserlogin = resource.internaluserlogin
				updateresource.aftpallowrandomsourceport = resource.aftpallowrandomsourceport
				updateresource.icaports = resource.icaports
				updateresource.tcpcip = resource.tcpcip
				updateresource.servicepathingressvlan = resource.servicepathingressvlan
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Timezone:
		CoordinatedUniversalTime = "CoordinatedUniversalTime"
		GMT_02_00_CEST_Europe_Andorra = "GMT+02:00-CEST-Europe/Andorra"
		GMT_04_00_GST_Asia_Dubai = "GMT+04:00-GST-Asia/Dubai"
		GMT_04_30_AFT_Asia_Kabul = "GMT+04:30-AFT-Asia/Kabul"
		GMT_04_00_AST_America_Antigua = "GMT-04:00-AST-America/Antigua"
		GMT_04_00_AST_America_Anguilla = "GMT-04:00-AST-America/Anguilla"
		GMT_02_00_CEST_Europe_Tirane = "GMT+02:00-CEST-Europe/Tirane"
		GMT_04_00__04_Asia_Yerevan = "GMT+04:00-+04-Asia/Yerevan"
		GMT_01_00_WAT_Africa_Luanda = "GMT+01:00-WAT-Africa/Luanda"
		GMT_12_00_NZST_Antarctica_McMurdo = "GMT+12:00-NZST-Antarctica/McMurdo"
		GMT_08_00__08_Antarctica_Casey = "GMT+08:00-+08-Antarctica/Casey"
		GMT_07_00__07_Antarctica_Davis = "GMT+07:00-+07-Antarctica/Davis"
		GMT_10_00__10_Antarctica_DumontDUrville = "GMT+10:00-+10-Antarctica/DumontDUrville"
		GMT_05_00__05_Antarctica_Mawson = "GMT+05:00-+05-Antarctica/Mawson"
		GMT_03_00_CLST_Antarctica_Palmer = "GMT-03:00-CLST-Antarctica/Palmer"
		GMT_03_00__03_Antarctica_Rothera = "GMT-03:00--03-Antarctica/Rothera"
		GMT_03_00__03_Antarctica_Syowa = "GMT+03:00-+03-Antarctica/Syowa"
		GMT_02_00__02_Antarctica_Troll = "GMT+02:00-+02-Antarctica/Troll"
		GMT_06_00__06_Antarctica_Vostok = "GMT+06:00-+06-Antarctica/Vostok"
		GMT_03_00_ART_America_Argentina_Buenos_Aires = "GMT-03:00-ART-America/Argentina/Buenos_Aires"
		GMT_03_00_ART_America_Argentina_Cordoba = "GMT-03:00-ART-America/Argentina/Cordoba"
		GMT_03_00_ART_America_Argentina_Salta = "GMT-03:00-ART-America/Argentina/Salta"
		GMT_03_00_ART_America_Argentina_Jujuy = "GMT-03:00-ART-America/Argentina/Jujuy"
		GMT_03_00_ART_America_Argentina_Tucuman = "GMT-03:00-ART-America/Argentina/Tucuman"
		GMT_03_00_ART_America_Argentina_Catamarca = "GMT-03:00-ART-America/Argentina/Catamarca"
		GMT_03_00_ART_America_Argentina_La_Rioja = "GMT-03:00-ART-America/Argentina/La_Rioja"
		GMT_03_00_ART_America_Argentina_San_Juan = "GMT-03:00-ART-America/Argentina/San_Juan"
		GMT_03_00_ART_America_Argentina_Mendoza = "GMT-03:00-ART-America/Argentina/Mendoza"
		GMT_03_00_ART_America_Argentina_San_Luis = "GMT-03:00-ART-America/Argentina/San_Luis"
		GMT_03_00_ART_America_Argentina_Rio_Gallegos = "GMT-03:00-ART-America/Argentina/Rio_Gallegos"
		GMT_03_00_ART_America_Argentina_Ushuaia = "GMT-03:00-ART-America/Argentina/Ushuaia"
		GMT_11_00_SST_Pacific_Pago_Pago = "GMT-11:00-SST-Pacific/Pago_Pago"
		GMT_02_00_CEST_Europe_Vienna = "GMT+02:00-CEST-Europe/Vienna"
		GMT_10_30_LHST_Australia_Lord_Howe = "GMT+10:30-LHST-Australia/Lord_Howe"
		GMT_11_00_MIST_Antarctica_Macquarie = "GMT+11:00-MIST-Antarctica/Macquarie"
		GMT_10_00_AEST_Australia_Hobart = "GMT+10:00-AEST-Australia/Hobart"
		GMT_10_00_AEST_Australia_Currie = "GMT+10:00-AEST-Australia/Currie"
		GMT_10_00_AEST_Australia_Melbourne = "GMT+10:00-AEST-Australia/Melbourne"
		GMT_10_00_AEST_Australia_Sydney = "GMT+10:00-AEST-Australia/Sydney"
		GMT_09_30_ACST_Australia_Broken_Hill = "GMT+09:30-ACST-Australia/Broken_Hill"
		GMT_10_00_AEST_Australia_Brisbane = "GMT+10:00-AEST-Australia/Brisbane"
		GMT_10_00_AEST_Australia_Lindeman = "GMT+10:00-AEST-Australia/Lindeman"
		GMT_09_30_ACST_Australia_Adelaide = "GMT+09:30-ACST-Australia/Adelaide"
		GMT_09_30_ACST_Australia_Darwin = "GMT+09:30-ACST-Australia/Darwin"
		GMT_08_00_AWST_Australia_Perth = "GMT+08:00-AWST-Australia/Perth"
		GMT_08_45_ACWST_Australia_Eucla = "GMT+08:45-ACWST-Australia/Eucla"
		GMT_04_00_AST_America_Aruba = "GMT-04:00-AST-America/Aruba"
		GMT_03_00_EEST_Europe_Mariehamn = "GMT+03:00-EEST-Europe/Mariehamn"
		GMT_04_00__04_Asia_Baku = "GMT+04:00-+04-Asia/Baku"
		GMT_02_00_CEST_Europe_Sarajevo = "GMT+02:00-CEST-Europe/Sarajevo"
		GMT_04_00_AST_America_Barbados = "GMT-04:00-AST-America/Barbados"
		GMT_06_00_BDT_Asia_Dhaka = "GMT+06:00-BDT-Asia/Dhaka"
		GMT_02_00_CEST_Europe_Brussels = "GMT+02:00-CEST-Europe/Brussels"
		GMT_00_00_GMT_Africa_Ouagadougou = "GMT+00:00-GMT-Africa/Ouagadougou"
		GMT_03_00_EEST_Europe_Sofia = "GMT+03:00-EEST-Europe/Sofia"
		GMT_03_00_AST_Asia_Bahrain = "GMT+03:00-AST-Asia/Bahrain"
		GMT_02_00_CAT_Africa_Bujumbura = "GMT+02:00-CAT-Africa/Bujumbura"
		GMT_01_00_WAT_Africa_Porto_Novo = "GMT+01:00-WAT-Africa/Porto-Novo"
		GMT_04_00_AST_America_St_Barthelemy = "GMT-04:00-AST-America/St_Barthelemy"
		GMT_03_00_ADT_Atlantic_Bermuda = "GMT-03:00-ADT-Atlantic/Bermuda"
		GMT_08_00_BNT_Asia_Brunei = "GMT+08:00-BNT-Asia/Brunei"
		GMT_04_00_BOT_America_La_Paz = "GMT-04:00-BOT-America/La_Paz"
		GMT_04_00_AST_America_Kralendijk = "GMT-04:00-AST-America/Kralendijk"
		GMT_02_00_FNT_America_Noronha = "GMT-02:00-FNT-America/Noronha"
		GMT_03_00_BRT_America_Belem = "GMT-03:00-BRT-America/Belem"
		GMT_03_00_BRT_America_Fortaleza = "GMT-03:00-BRT-America/Fortaleza"
		GMT_03_00_BRT_America_Recife = "GMT-03:00-BRT-America/Recife"
		GMT_03_00_BRT_America_Araguaina = "GMT-03:00-BRT-America/Araguaina"
		GMT_03_00_BRT_America_Maceio = "GMT-03:00-BRT-America/Maceio"
		GMT_03_00_BRT_America_Bahia = "GMT-03:00-BRT-America/Bahia"
		GMT_03_00_BRT_America_Sao_Paulo = "GMT-03:00-BRT-America/Sao_Paulo"
		GMT_04_00_AMT_America_Campo_Grande = "GMT-04:00-AMT-America/Campo_Grande"
		GMT_04_00_AMT_America_Cuiaba = "GMT-04:00-AMT-America/Cuiaba"
		GMT_03_00_BRT_America_Santarem = "GMT-03:00-BRT-America/Santarem"
		GMT_04_00_AMT_America_Porto_Velho = "GMT-04:00-AMT-America/Porto_Velho"
		GMT_04_00_AMT_America_Boa_Vista = "GMT-04:00-AMT-America/Boa_Vista"
		GMT_04_00_AMT_America_Manaus = "GMT-04:00-AMT-America/Manaus"
		GMT_05_00_ACT_America_Eirunepe = "GMT-05:00-ACT-America/Eirunepe"
		GMT_05_00_ACT_America_Rio_Branco = "GMT-05:00-ACT-America/Rio_Branco"
		GMT_04_00_EDT_America_Nassau = "GMT-04:00-EDT-America/Nassau"
		GMT_06_00_BTT_Asia_Thimphu = "GMT+06:00-BTT-Asia/Thimphu"
		GMT_02_00_CAT_Africa_Gaborone = "GMT+02:00-CAT-Africa/Gaborone"
		GMT_03_00__03_Europe_Minsk = "GMT+03:00-+03-Europe/Minsk"
		GMT_06_00_CST_America_Belize = "GMT-06:00-CST-America/Belize"
		GMT_02_30_NDT_America_St_Johns = "GMT-02:30-NDT-America/St_Johns"
		GMT_03_00_ADT_America_Halifax = "GMT-03:00-ADT-America/Halifax"
		GMT_03_00_ADT_America_Glace_Bay = "GMT-03:00-ADT-America/Glace_Bay"
		GMT_03_00_ADT_America_Moncton = "GMT-03:00-ADT-America/Moncton"
		GMT_03_00_ADT_America_Goose_Bay = "GMT-03:00-ADT-America/Goose_Bay"
		GMT_04_00_AST_America_Blanc_Sablon = "GMT-04:00-AST-America/Blanc-Sablon"
		GMT_04_00_EDT_America_Toronto = "GMT-04:00-EDT-America/Toronto"
		GMT_04_00_EDT_America_Nipigon = "GMT-04:00-EDT-America/Nipigon"
		GMT_04_00_EDT_America_Thunder_Bay = "GMT-04:00-EDT-America/Thunder_Bay"
		GMT_04_00_EDT_America_Iqaluit = "GMT-04:00-EDT-America/Iqaluit"
		GMT_04_00_EDT_America_Pangnirtung = "GMT-04:00-EDT-America/Pangnirtung"
		GMT_05_00_EST_America_Atikokan = "GMT-05:00-EST-America/Atikokan"
		GMT_05_00_CDT_America_Winnipeg = "GMT-05:00-CDT-America/Winnipeg"
		GMT_05_00_CDT_America_Rainy_River = "GMT-05:00-CDT-America/Rainy_River"
		GMT_05_00_CDT_America_Resolute = "GMT-05:00-CDT-America/Resolute"
		GMT_05_00_CDT_America_Rankin_Inlet = "GMT-05:00-CDT-America/Rankin_Inlet"
		GMT_06_00_CST_America_Regina = "GMT-06:00-CST-America/Regina"
		GMT_06_00_CST_America_Swift_Current = "GMT-06:00-CST-America/Swift_Current"
		GMT_06_00_MDT_America_Edmonton = "GMT-06:00-MDT-America/Edmonton"
		GMT_06_00_MDT_America_Cambridge_Bay = "GMT-06:00-MDT-America/Cambridge_Bay"
		GMT_06_00_MDT_America_Yellowknife = "GMT-06:00-MDT-America/Yellowknife"
		GMT_06_00_MDT_America_Inuvik = "GMT-06:00-MDT-America/Inuvik"
		GMT_07_00_MST_America_Creston = "GMT-07:00-MST-America/Creston"
		GMT_07_00_MST_America_Dawson_Creek = "GMT-07:00-MST-America/Dawson_Creek"
		GMT_07_00_MST_America_Fort_Nelson = "GMT-07:00-MST-America/Fort_Nelson"
		GMT_07_00_PDT_America_Vancouver = "GMT-07:00-PDT-America/Vancouver"
		GMT_07_00_PDT_America_Whitehorse = "GMT-07:00-PDT-America/Whitehorse"
		GMT_07_00_PDT_America_Dawson = "GMT-07:00-PDT-America/Dawson"
		GMT_06_30_CCT_Indian_Cocos = "GMT+06:30-CCT-Indian/Cocos"
		GMT_01_00_WAT_Africa_Kinshasa = "GMT+01:00-WAT-Africa/Kinshasa"
		GMT_02_00_CAT_Africa_Lubumbashi = "GMT+02:00-CAT-Africa/Lubumbashi"
		GMT_01_00_WAT_Africa_Bangui = "GMT+01:00-WAT-Africa/Bangui"
		GMT_01_00_WAT_Africa_Brazzaville = "GMT+01:00-WAT-Africa/Brazzaville"
		GMT_02_00_CEST_Europe_Zurich = "GMT+02:00-CEST-Europe/Zurich"
		GMT_00_00_GMT_Africa_Abidjan = "GMT+00:00-GMT-Africa/Abidjan"
		GMT_10_00_CKT_Pacific_Rarotonga = "GMT-10:00-CKT-Pacific/Rarotonga"
		GMT_03_00_CLST_America_Santiago = "GMT-03:00-CLST-America/Santiago"
		GMT_05_00_EASST_Pacific_Easter = "GMT-05:00-EASST-Pacific/Easter"
		GMT_01_00_WAT_Africa_Douala = "GMT+01:00-WAT-Africa/Douala"
		GMT_08_00_CST_Asia_Shanghai = "GMT+08:00-CST-Asia/Shanghai"
		GMT_06_00_XJT_Asia_Urumqi = "GMT+06:00-XJT-Asia/Urumqi"
		GMT_05_00_COT_America_Bogota = "GMT-05:00-COT-America/Bogota"
		GMT_06_00_CST_America_Costa_Rica = "GMT-06:00-CST-America/Costa_Rica"
		GMT_04_00_CDT_America_Havana = "GMT-04:00-CDT-America/Havana"
		GMT_01_00_CVT_Atlantic_Cape_Verde = "GMT-01:00-CVT-Atlantic/Cape_Verde"
		GMT_04_00_AST_America_Curacao = "GMT-04:00-AST-America/Curacao"
		GMT_07_00_CXT_Indian_Christmas = "GMT+07:00-CXT-Indian/Christmas"
		GMT_03_00_EEST_Asia_Nicosia = "GMT+03:00-EEST-Asia/Nicosia"
		GMT_02_00_CEST_Europe_Prague = "GMT+02:00-CEST-Europe/Prague"
		GMT_02_00_CEST_Europe_Berlin = "GMT+02:00-CEST-Europe/Berlin"
		GMT_02_00_CEST_Europe_Busingen = "GMT+02:00-CEST-Europe/Busingen"
		GMT_03_00_EAT_Africa_Djibouti = "GMT+03:00-EAT-Africa/Djibouti"
		GMT_02_00_CEST_Europe_Copenhagen = "GMT+02:00-CEST-Europe/Copenhagen"
		GMT_04_00_AST_America_Dominica = "GMT-04:00-AST-America/Dominica"
		GMT_04_00_AST_America_Santo_Domingo = "GMT-04:00-AST-America/Santo_Domingo"
		GMT_01_00_CET_Africa_Algiers = "GMT+01:00-CET-Africa/Algiers"
		GMT_05_00_ECT_America_Guayaquil = "GMT-05:00-ECT-America/Guayaquil"
		GMT_06_00_GALT_Pacific_Galapagos = "GMT-06:00-GALT-Pacific/Galapagos"
		GMT_03_00_EEST_Europe_Tallinn = "GMT+03:00-EEST-Europe/Tallinn"
		GMT_02_00_EET_Africa_Cairo = "GMT+02:00-EET-Africa/Cairo"
		GMT_01_00_WEST_Africa_El_Aaiun = "GMT+01:00-WEST-Africa/El_Aaiun"
		GMT_03_00_EAT_Africa_Asmara = "GMT+03:00-EAT-Africa/Asmara"
		GMT_02_00_CEST_Europe_Madrid = "GMT+02:00-CEST-Europe/Madrid"
		GMT_02_00_CEST_Africa_Ceuta = "GMT+02:00-CEST-Africa/Ceuta"
		GMT_01_00_WEST_Atlantic_Canary = "GMT+01:00-WEST-Atlantic/Canary"
		GMT_03_00_EAT_Africa_Addis_Ababa = "GMT+03:00-EAT-Africa/Addis_Ababa"
		GMT_03_00_EEST_Europe_Helsinki = "GMT+03:00-EEST-Europe/Helsinki"
		GMT_12_00_FJT_Pacific_Fiji = "GMT+12:00-FJT-Pacific/Fiji"
		GMT_03_00_FKST_Atlantic_Stanley = "GMT-03:00-FKST-Atlantic/Stanley"
		GMT_10_00_CHUT_Pacific_Chuuk = "GMT+10:00-CHUT-Pacific/Chuuk"
		GMT_11_00_PONT_Pacific_Pohnpei = "GMT+11:00-PONT-Pacific/Pohnpei"
		GMT_11_00_KOST_Pacific_Kosrae = "GMT+11:00-KOST-Pacific/Kosrae"
		GMT_01_00_WEST_Atlantic_Faroe = "GMT+01:00-WEST-Atlantic/Faroe"
		GMT_02_00_CEST_Europe_Paris = "GMT+02:00-CEST-Europe/Paris"
		GMT_01_00_WAT_Africa_Libreville = "GMT+01:00-WAT-Africa/Libreville"
		GMT_01_00_BST_Europe_London = "GMT+01:00-BST-Europe/London"
		GMT_04_00_AST_America_Grenada = "GMT-04:00-AST-America/Grenada"
		GMT_04_00__04_Asia_Tbilisi = "GMT+04:00-+04-Asia/Tbilisi"
		GMT_03_00_GFT_America_Cayenne = "GMT-03:00-GFT-America/Cayenne"
		GMT_01_00_BST_Europe_Guernsey = "GMT+01:00-BST-Europe/Guernsey"
		GMT_00_00_GMT_Africa_Accra = "GMT+00:00-GMT-Africa/Accra"
		GMT_02_00_CEST_Europe_Gibraltar = "GMT+02:00-CEST-Europe/Gibraltar"
		GMT_02_00_WGST_America_Godthab = "GMT-02:00-WGST-America/Godthab"
		GMT_00_00_GMT_America_Danmarkshavn = "GMT+00:00-GMT-America/Danmarkshavn"
		GMT_00_00_EGST_America_Scoresbysund = "GMT+00:00-EGST-America/Scoresbysund"
		GMT_03_00_ADT_America_Thule = "GMT-03:00-ADT-America/Thule"
		GMT_00_00_GMT_Africa_Banjul = "GMT+00:00-GMT-Africa/Banjul"
		GMT_00_00_GMT_Africa_Conakry = "GMT+00:00-GMT-Africa/Conakry"
		GMT_04_00_AST_America_Guadeloupe = "GMT-04:00-AST-America/Guadeloupe"
		GMT_01_00_WAT_Africa_Malabo = "GMT+01:00-WAT-Africa/Malabo"
		GMT_03_00_EEST_Europe_Athens = "GMT+03:00-EEST-Europe/Athens"
		GMT_02_00_GST_Atlantic_South_Georgia = "GMT-02:00-GST-Atlantic/South_Georgia"
		GMT_06_00_CST_America_Guatemala = "GMT-06:00-CST-America/Guatemala"
		GMT_10_00_ChST_Pacific_Guam = "GMT+10:00-ChST-Pacific/Guam"
		GMT_00_00_GMT_Africa_Bissau = "GMT+00:00-GMT-Africa/Bissau"
		GMT_04_00_GYT_America_Guyana = "GMT-04:00-GYT-America/Guyana"
		GMT_08_00_HKT_Asia_Hong_Kong = "GMT+08:00-HKT-Asia/Hong_Kong"
		GMT_06_00_CST_America_Tegucigalpa = "GMT-06:00-CST-America/Tegucigalpa"
		GMT_02_00_CEST_Europe_Zagreb = "GMT+02:00-CEST-Europe/Zagreb"
		GMT_05_00_EST_America_Port_au_Prince = "GMT-05:00-EST-America/Port-au-Prince"
		GMT_02_00_CEST_Europe_Budapest = "GMT+02:00-CEST-Europe/Budapest"
		GMT_07_00_WIB_Asia_Jakarta = "GMT+07:00-WIB-Asia/Jakarta"
		GMT_07_00_WIB_Asia_Pontianak = "GMT+07:00-WIB-Asia/Pontianak"
		GMT_08_00_WITA_Asia_Makassar = "GMT+08:00-WITA-Asia/Makassar"
		GMT_09_00_WIT_Asia_Jayapura = "GMT+09:00-WIT-Asia/Jayapura"
		GMT_01_00_IST_Europe_Dublin = "GMT+01:00-IST-Europe/Dublin"
		GMT_03_00_IDT_Asia_Jerusalem = "GMT+03:00-IDT-Asia/Jerusalem"
		GMT_01_00_BST_Europe_Isle_of_Man = "GMT+01:00-BST-Europe/Isle_of_Man"
		GMT_05_30_IST_Asia_Kolkata = "GMT+05:30-IST-Asia/Kolkata"
		GMT_06_00_IOT_Indian_Chagos = "GMT+06:00-IOT-Indian/Chagos"
		GMT_03_00_AST_Asia_Baghdad = "GMT+03:00-AST-Asia/Baghdad"
		GMT_04_30_IRDT_Asia_Tehran = "GMT+04:30-IRDT-Asia/Tehran"
		GMT_00_00_GMT_Atlantic_Reykjavik = "GMT+00:00-GMT-Atlantic/Reykjavik"
		GMT_02_00_CEST_Europe_Rome = "GMT+02:00-CEST-Europe/Rome"
		GMT_01_00_BST_Europe_Jersey = "GMT+01:00-BST-Europe/Jersey"
		GMT_05_00_EST_America_Jamaica = "GMT-05:00-EST-America/Jamaica"
		GMT_03_00_EEST_Asia_Amman = "GMT+03:00-EEST-Asia/Amman"
		GMT_09_00_JST_Asia_Tokyo = "GMT+09:00-JST-Asia/Tokyo"
		GMT_03_00_EAT_Africa_Nairobi = "GMT+03:00-EAT-Africa/Nairobi"
		GMT_06_00__06_Asia_Bishkek = "GMT+06:00-+06-Asia/Bishkek"
		GMT_07_00_ICT_Asia_Phnom_Penh = "GMT+07:00-ICT-Asia/Phnom_Penh"
		GMT_12_00_GILT_Pacific_Tarawa = "GMT+12:00-GILT-Pacific/Tarawa"
		GMT_13_00_PHOT_Pacific_Enderbury = "GMT+13:00-PHOT-Pacific/Enderbury"
		GMT_14_00_LINT_Pacific_Kiritimati = "GMT+14:00-LINT-Pacific/Kiritimati"
		GMT_03_00_EAT_Indian_Comoro = "GMT+03:00-EAT-Indian/Comoro"
		GMT_04_00_AST_America_St_Kitts = "GMT-04:00-AST-America/St_Kitts"
		GMT_08_30_KST_Asia_Pyongyang = "GMT+08:30-KST-Asia/Pyongyang"
		GMT_09_00_KST_Asia_Seoul = "GMT+09:00-KST-Asia/Seoul"
		GMT_03_00_AST_Asia_Kuwait = "GMT+03:00-AST-Asia/Kuwait"
		GMT_05_00_EST_America_Cayman = "GMT-05:00-EST-America/Cayman"
		GMT_06_00__06_Asia_Almaty = "GMT+06:00-+06-Asia/Almaty"
		GMT_06_00__06_Asia_Qyzylorda = "GMT+06:00-+06-Asia/Qyzylorda"
		GMT_05_00__05_Asia_Aqtobe = "GMT+05:00-+05-Asia/Aqtobe"
		GMT_05_00__05_Asia_Aqtau = "GMT+05:00-+05-Asia/Aqtau"
		GMT_05_00__05_Asia_Oral = "GMT+05:00-+05-Asia/Oral"
		GMT_07_00_ICT_Asia_Vientiane = "GMT+07:00-ICT-Asia/Vientiane"
		GMT_03_00_EEST_Asia_Beirut = "GMT+03:00-EEST-Asia/Beirut"
		GMT_04_00_AST_America_St_Lucia = "GMT-04:00-AST-America/St_Lucia"
		GMT_02_00_CEST_Europe_Vaduz = "GMT+02:00-CEST-Europe/Vaduz"
		GMT_05_30_IST_Asia_Colombo = "GMT+05:30-IST-Asia/Colombo"
		GMT_00_00_GMT_Africa_Monrovia = "GMT+00:00-GMT-Africa/Monrovia"
		GMT_02_00_SAST_Africa_Maseru = "GMT+02:00-SAST-Africa/Maseru"
		GMT_03_00_EEST_Europe_Vilnius = "GMT+03:00-EEST-Europe/Vilnius"
		GMT_02_00_CEST_Europe_Luxembourg = "GMT+02:00-CEST-Europe/Luxembourg"
		GMT_03_00_EEST_Europe_Riga = "GMT+03:00-EEST-Europe/Riga"
		GMT_02_00_EET_Africa_Tripoli = "GMT+02:00-EET-Africa/Tripoli"
		GMT_01_00_WEST_Africa_Casablanca = "GMT+01:00-WEST-Africa/Casablanca"
		GMT_02_00_CEST_Europe_Monaco = "GMT+02:00-CEST-Europe/Monaco"
		GMT_03_00_EEST_Europe_Chisinau = "GMT+03:00-EEST-Europe/Chisinau"
		GMT_02_00_CEST_Europe_Podgorica = "GMT+02:00-CEST-Europe/Podgorica"
		GMT_04_00_AST_America_Marigot = "GMT-04:00-AST-America/Marigot"
		GMT_03_00_EAT_Indian_Antananarivo = "GMT+03:00-EAT-Indian/Antananarivo"
		GMT_12_00_MHT_Pacific_Majuro = "GMT+12:00-MHT-Pacific/Majuro"
		GMT_12_00_MHT_Pacific_Kwajalein = "GMT+12:00-MHT-Pacific/Kwajalein"
		GMT_02_00_CEST_Europe_Skopje = "GMT+02:00-CEST-Europe/Skopje"
		GMT_00_00_GMT_Africa_Bamako = "GMT+00:00-GMT-Africa/Bamako"
		GMT_06_30_MMT_Asia_Yangon = "GMT+06:30-MMT-Asia/Yangon"
		GMT_09_00_ULAST_Asia_Ulaanbaatar = "GMT+09:00-ULAST-Asia/Ulaanbaatar"
		GMT_08_00_HOVST_Asia_Hovd = "GMT+08:00-HOVST-Asia/Hovd"
		GMT_09_00_CHOST_Asia_Choibalsan = "GMT+09:00-CHOST-Asia/Choibalsan"
		GMT_08_00_CST_Asia_Macau = "GMT+08:00-CST-Asia/Macau"
		GMT_10_00_ChST_Pacific_Saipan = "GMT+10:00-ChST-Pacific/Saipan"
		GMT_04_00_AST_America_Martinique = "GMT-04:00-AST-America/Martinique"
		GMT_00_00_GMT_Africa_Nouakchott = "GMT+00:00-GMT-Africa/Nouakchott"
		GMT_04_00_AST_America_Montserrat = "GMT-04:00-AST-America/Montserrat"
		GMT_02_00_CEST_Europe_Malta = "GMT+02:00-CEST-Europe/Malta"
		GMT_04_00_MUT_Indian_Mauritius = "GMT+04:00-MUT-Indian/Mauritius"
		GMT_05_00_MVT_Indian_Maldives = "GMT+05:00-MVT-Indian/Maldives"
		GMT_02_00_CAT_Africa_Blantyre = "GMT+02:00-CAT-Africa/Blantyre"
		GMT_05_00_CDT_America_Mexico_City = "GMT-05:00-CDT-America/Mexico_City"
		GMT_05_00_EST_America_Cancun = "GMT-05:00-EST-America/Cancun"
		GMT_05_00_CDT_America_Merida = "GMT-05:00-CDT-America/Merida"
		GMT_05_00_CDT_America_Monterrey = "GMT-05:00-CDT-America/Monterrey"
		GMT_05_00_CDT_America_Matamoros = "GMT-05:00-CDT-America/Matamoros"
		GMT_06_00_MDT_America_Mazatlan = "GMT-06:00-MDT-America/Mazatlan"
		GMT_06_00_MDT_America_Chihuahua = "GMT-06:00-MDT-America/Chihuahua"
		GMT_06_00_MDT_America_Ojinaga = "GMT-06:00-MDT-America/Ojinaga"
		GMT_07_00_MST_America_Hermosillo = "GMT-07:00-MST-America/Hermosillo"
		GMT_07_00_PDT_America_Tijuana = "GMT-07:00-PDT-America/Tijuana"
		GMT_05_00_CDT_America_Bahia_Banderas = "GMT-05:00-CDT-America/Bahia_Banderas"
		GMT_08_00_MYT_Asia_Kuala_Lumpur = "GMT+08:00-MYT-Asia/Kuala_Lumpur"
		GMT_08_00_MYT_Asia_Kuching = "GMT+08:00-MYT-Asia/Kuching"
		GMT_02_00_CAT_Africa_Maputo = "GMT+02:00-CAT-Africa/Maputo"
		GMT_01_00_WAT_Africa_Windhoek = "GMT+01:00-WAT-Africa/Windhoek"
		GMT_11_00_NCT_Pacific_Noumea = "GMT+11:00-NCT-Pacific/Noumea"
		GMT_01_00_WAT_Africa_Niamey = "GMT+01:00-WAT-Africa/Niamey"
		GMT_11_00_NFT_Pacific_Norfolk = "GMT+11:00-NFT-Pacific/Norfolk"
		GMT_01_00_WAT_Africa_Lagos = "GMT+01:00-WAT-Africa/Lagos"
		GMT_06_00_CST_America_Managua = "GMT-06:00-CST-America/Managua"
		GMT_02_00_CEST_Europe_Amsterdam = "GMT+02:00-CEST-Europe/Amsterdam"
		GMT_02_00_CEST_Europe_Oslo = "GMT+02:00-CEST-Europe/Oslo"
		GMT_05_45_NPT_Asia_Kathmandu = "GMT+05:45-NPT-Asia/Kathmandu"
		GMT_12_00_NRT_Pacific_Nauru = "GMT+12:00-NRT-Pacific/Nauru"
		GMT_11_00_NUT_Pacific_Niue = "GMT-11:00-NUT-Pacific/Niue"
		GMT_12_00_NZST_Pacific_Auckland = "GMT+12:00-NZST-Pacific/Auckland"
		GMT_12_45_CHAST_Pacific_Chatham = "GMT+12:45-CHAST-Pacific/Chatham"
		GMT_04_00_GST_Asia_Muscat = "GMT+04:00-GST-Asia/Muscat"
		GMT_05_00_EST_America_Panama = "GMT-05:00-EST-America/Panama"
		GMT_05_00_PET_America_Lima = "GMT-05:00-PET-America/Lima"
		GMT_10_00_TAHT_Pacific_Tahiti = "GMT-10:00-TAHT-Pacific/Tahiti"
		GMT_09_30_MART_Pacific_Marquesas = "GMT-09:30-MART-Pacific/Marquesas"
		GMT_09_00_GAMT_Pacific_Gambier = "GMT-09:00-GAMT-Pacific/Gambier"
		GMT_10_00_PGT_Pacific_Port_Moresby = "GMT+10:00-PGT-Pacific/Port_Moresby"
		GMT_11_00_BST_Pacific_Bougainville = "GMT+11:00-BST-Pacific/Bougainville"
		GMT_08_00_PHT_Asia_Manila = "GMT+08:00-PHT-Asia/Manila"
		GMT_05_00_PKT_Asia_Karachi = "GMT+05:00-PKT-Asia/Karachi"
		GMT_02_00_CEST_Europe_Warsaw = "GMT+02:00-CEST-Europe/Warsaw"
		GMT_02_00_PMDT_America_Miquelon = "GMT-02:00-PMDT-America/Miquelon"
		GMT_08_00_PST_Pacific_Pitcairn = "GMT-08:00-PST-Pacific/Pitcairn"
		GMT_04_00_AST_America_Puerto_Rico = "GMT-04:00-AST-America/Puerto_Rico"
		GMT_03_00_EEST_Asia_Gaza = "GMT+03:00-EEST-Asia/Gaza"
		GMT_03_00_EEST_Asia_Hebron = "GMT+03:00-EEST-Asia/Hebron"
		GMT_01_00_WEST_Europe_Lisbon = "GMT+01:00-WEST-Europe/Lisbon"
		GMT_01_00_WEST_Atlantic_Madeira = "GMT+01:00-WEST-Atlantic/Madeira"
		GMT_00_00_AZOST_Atlantic_Azores = "GMT+00:00-AZOST-Atlantic/Azores"
		GMT_09_00_PWT_Pacific_Palau = "GMT+09:00-PWT-Pacific/Palau"
		GMT_04_00_PYT_America_Asuncion = "GMT-04:00-PYT-America/Asuncion"
		GMT_03_00_AST_Asia_Qatar = "GMT+03:00-AST-Asia/Qatar"
		GMT_04_00_RET_Indian_Reunion = "GMT+04:00-RET-Indian/Reunion"
		GMT_03_00_EEST_Europe_Bucharest = "GMT+03:00-EEST-Europe/Bucharest"
		GMT_02_00_CEST_Europe_Belgrade = "GMT+02:00-CEST-Europe/Belgrade"
		GMT_02_00_EET_Europe_Kaliningrad = "GMT+02:00-EET-Europe/Kaliningrad"
		GMT_03_00_MSK_Europe_Moscow = "GMT+03:00-MSK-Europe/Moscow"
		GMT_03_00_MSK_Europe_Simferopol = "GMT+03:00-MSK-Europe/Simferopol"
		GMT_03_00__03_Europe_Volgograd = "GMT+03:00-+03-Europe/Volgograd"
		GMT_03_00__03_Europe_Kirov = "GMT+03:00-+03-Europe/Kirov"
		GMT_04_00__04_Europe_Astrakhan = "GMT+04:00-+04-Europe/Astrakhan"
		GMT_04_00__04_Europe_Samara = "GMT+04:00-+04-Europe/Samara"
		GMT_04_00__04_Europe_Ulyanovsk = "GMT+04:00-+04-Europe/Ulyanovsk"
		GMT_05_00__05_Asia_Yekaterinburg = "GMT+05:00-+05-Asia/Yekaterinburg"
		GMT_06_00__06_Asia_Omsk = "GMT+06:00-+06-Asia/Omsk"
		GMT_07_00__07_Asia_Novosibirsk = "GMT+07:00-+07-Asia/Novosibirsk"
		GMT_07_00__07_Asia_Barnaul = "GMT+07:00-+07-Asia/Barnaul"
		GMT_07_00__07_Asia_Tomsk = "GMT+07:00-+07-Asia/Tomsk"
		GMT_07_00__07_Asia_Novokuznetsk = "GMT+07:00-+07-Asia/Novokuznetsk"
		GMT_07_00__07_Asia_Krasnoyarsk = "GMT+07:00-+07-Asia/Krasnoyarsk"
		GMT_08_00__08_Asia_Irkutsk = "GMT+08:00-+08-Asia/Irkutsk"
		GMT_09_00__09_Asia_Chita = "GMT+09:00-+09-Asia/Chita"
		GMT_09_00__09_Asia_Yakutsk = "GMT+09:00-+09-Asia/Yakutsk"
		GMT_09_00__09_Asia_Khandyga = "GMT+09:00-+09-Asia/Khandyga"
		GMT_10_00__10_Asia_Vladivostok = "GMT+10:00-+10-Asia/Vladivostok"
		GMT_10_00__10_Asia_Ust_Nera = "GMT+10:00-+10-Asia/Ust-Nera"
		GMT_11_00__11_Asia_Magadan = "GMT+11:00-+11-Asia/Magadan"
		GMT_11_00__11_Asia_Sakhalin = "GMT+11:00-+11-Asia/Sakhalin"
		GMT_11_00__11_Asia_Srednekolymsk = "GMT+11:00-+11-Asia/Srednekolymsk"
		GMT_12_00__12_Asia_Kamchatka = "GMT+12:00-+12-Asia/Kamchatka"
		GMT_12_00__12_Asia_Anadyr = "GMT+12:00-+12-Asia/Anadyr"
		GMT_02_00_CAT_Africa_Kigali = "GMT+02:00-CAT-Africa/Kigali"
		GMT_03_00_AST_Asia_Riyadh = "GMT+03:00-AST-Asia/Riyadh"
		GMT_11_00_SBT_Pacific_Guadalcanal = "GMT+11:00-SBT-Pacific/Guadalcanal"
		GMT_04_00_SCT_Indian_Mahe = "GMT+04:00-SCT-Indian/Mahe"
		GMT_03_00_EAT_Africa_Khartoum = "GMT+03:00-EAT-Africa/Khartoum"
		GMT_02_00_CEST_Europe_Stockholm = "GMT+02:00-CEST-Europe/Stockholm"
		GMT_08_00_SGT_Asia_Singapore = "GMT+08:00-SGT-Asia/Singapore"
		GMT_00_00_GMT_Atlantic_St_Helena = "GMT+00:00-GMT-Atlantic/St_Helena"
		GMT_02_00_CEST_Europe_Ljubljana = "GMT+02:00-CEST-Europe/Ljubljana"
		GMT_02_00_CEST_Arctic_Longyearbyen = "GMT+02:00-CEST-Arctic/Longyearbyen"
		GMT_02_00_CEST_Europe_Bratislava = "GMT+02:00-CEST-Europe/Bratislava"
		GMT_00_00_GMT_Africa_Freetown = "GMT+00:00-GMT-Africa/Freetown"
		GMT_02_00_CEST_Europe_San_Marino = "GMT+02:00-CEST-Europe/San_Marino"
		GMT_00_00_GMT_Africa_Dakar = "GMT+00:00-GMT-Africa/Dakar"
		GMT_03_00_EAT_Africa_Mogadishu = "GMT+03:00-EAT-Africa/Mogadishu"
		GMT_03_00_SRT_America_Paramaribo = "GMT-03:00-SRT-America/Paramaribo"
		GMT_03_00_EAT_Africa_Juba = "GMT+03:00-EAT-Africa/Juba"
		GMT_00_00_GMT_Africa_Sao_Tome = "GMT+00:00-GMT-Africa/Sao_Tome"
		GMT_06_00_CST_America_El_Salvador = "GMT-06:00-CST-America/El_Salvador"
		GMT_04_00_AST_America_Lower_Princes = "GMT-04:00-AST-America/Lower_Princes"
		GMT_03_00_EEST_Asia_Damascus = "GMT+03:00-EEST-Asia/Damascus"
		GMT_02_00_SAST_Africa_Mbabane = "GMT+02:00-SAST-Africa/Mbabane"
		GMT_04_00_AST_America_Grand_Turk = "GMT-04:00-AST-America/Grand_Turk"
		GMT_01_00_WAT_Africa_Ndjamena = "GMT+01:00-WAT-Africa/Ndjamena"
		GMT_05_00__05_Indian_Kerguelen = "GMT+05:00-+05-Indian/Kerguelen"
		GMT_00_00_GMT_Africa_Lome = "GMT+00:00-GMT-Africa/Lome"
		GMT_07_00_ICT_Asia_Bangkok = "GMT+07:00-ICT-Asia/Bangkok"
		GMT_05_00__05_Asia_Dushanbe = "GMT+05:00-+05-Asia/Dushanbe"
		GMT_13_00_TKT_Pacific_Fakaofo = "GMT+13:00-TKT-Pacific/Fakaofo"
		GMT_09_00_TLT_Asia_Dili = "GMT+09:00-TLT-Asia/Dili"
		GMT_05_00__05_Asia_Ashgabat = "GMT+05:00-+05-Asia/Ashgabat"
		GMT_01_00_CET_Africa_Tunis = "GMT+01:00-CET-Africa/Tunis"
		GMT_13_00_TOT_Pacific_Tongatapu = "GMT+13:00-TOT-Pacific/Tongatapu"
		GMT_03_00__03_Europe_Istanbul = "GMT+03:00-+03-Europe/Istanbul"
		GMT_04_00_AST_America_Port_of_Spain = "GMT-04:00-AST-America/Port_of_Spain"
		GMT_12_00_TVT_Pacific_Funafuti = "GMT+12:00-TVT-Pacific/Funafuti"
		GMT_08_00_CST_Asia_Taipei = "GMT+08:00-CST-Asia/Taipei"
		GMT_03_00_EAT_Africa_Dar_es_Salaam = "GMT+03:00-EAT-Africa/Dar_es_Salaam"
		GMT_03_00_EEST_Europe_Kiev = "GMT+03:00-EEST-Europe/Kiev"
		GMT_03_00_EEST_Europe_Uzhgorod = "GMT+03:00-EEST-Europe/Uzhgorod"
		GMT_03_00_EEST_Europe_Zaporozhye = "GMT+03:00-EEST-Europe/Zaporozhye"
		GMT_03_00_EAT_Africa_Kampala = "GMT+03:00-EAT-Africa/Kampala"
		GMT_10_00_HST_Pacific_Johnston = "GMT-10:00-HST-Pacific/Johnston"
		GMT_11_00_SST_Pacific_Midway = "GMT-11:00-SST-Pacific/Midway"
		GMT_12_00_WAKT_Pacific_Wake = "GMT+12:00-WAKT-Pacific/Wake"
		GMT_04_00_EDT_America_New_York = "GMT-04:00-EDT-America/New_York"
		GMT_04_00_EDT_America_Detroit = "GMT-04:00-EDT-America/Detroit"
		GMT_04_00_EDT_America_Kentucky_Louisville = "GMT-04:00-EDT-America/Kentucky/Louisville"
		GMT_04_00_EDT_America_Kentucky_Monticello = "GMT-04:00-EDT-America/Kentucky/Monticello"
		GMT_04_00_EDT_America_Indiana_Indianapolis = "GMT-04:00-EDT-America/Indiana/Indianapolis"
		GMT_04_00_EDT_America_Indiana_Vincennes = "GMT-04:00-EDT-America/Indiana/Vincennes"
		GMT_04_00_EDT_America_Indiana_Winamac = "GMT-04:00-EDT-America/Indiana/Winamac"
		GMT_04_00_EDT_America_Indiana_Marengo = "GMT-04:00-EDT-America/Indiana/Marengo"
		GMT_04_00_EDT_America_Indiana_Petersburg = "GMT-04:00-EDT-America/Indiana/Petersburg"
		GMT_04_00_EDT_America_Indiana_Vevay = "GMT-04:00-EDT-America/Indiana/Vevay"
		GMT_05_00_CDT_America_Chicago = "GMT-05:00-CDT-America/Chicago"
		GMT_05_00_CDT_America_Indiana_Tell_City = "GMT-05:00-CDT-America/Indiana/Tell_City"
		GMT_05_00_CDT_America_Indiana_Knox = "GMT-05:00-CDT-America/Indiana/Knox"
		GMT_05_00_CDT_America_Menominee = "GMT-05:00-CDT-America/Menominee"
		GMT_05_00_CDT_America_North_Dakota_Center = "GMT-05:00-CDT-America/North_Dakota/Center"
		GMT_05_00_CDT_America_North_Dakota_New_Salem = "GMT-05:00-CDT-America/North_Dakota/New_Salem"
		GMT_05_00_CDT_America_North_Dakota_Beulah = "GMT-05:00-CDT-America/North_Dakota/Beulah"
		GMT_06_00_MDT_America_Denver = "GMT-06:00-MDT-America/Denver"
		GMT_06_00_MDT_America_Boise = "GMT-06:00-MDT-America/Boise"
		GMT_07_00_MST_America_Phoenix = "GMT-07:00-MST-America/Phoenix"
		GMT_07_00_PDT_America_Los_Angeles = "GMT-07:00-PDT-America/Los_Angeles"
		GMT_08_00_AKDT_America_Anchorage = "GMT-08:00-AKDT-America/Anchorage"
		GMT_08_00_AKDT_America_Juneau = "GMT-08:00-AKDT-America/Juneau"
		GMT_08_00_AKDT_America_Sitka = "GMT-08:00-AKDT-America/Sitka"
		GMT_08_00_AKDT_America_Metlakatla = "GMT-08:00-AKDT-America/Metlakatla"
		GMT_08_00_AKDT_America_Yakutat = "GMT-08:00-AKDT-America/Yakutat"
		GMT_08_00_AKDT_America_Nome = "GMT-08:00-AKDT-America/Nome"
		GMT_09_00_HDT_America_Adak = "GMT-09:00-HDT-America/Adak"
		GMT_10_00_HST_Pacific_Honolulu = "GMT-10:00-HST-Pacific/Honolulu"
		GMT_03_00_UYT_America_Montevideo = "GMT-03:00-UYT-America/Montevideo"
		GMT_05_00__05_Asia_Samarkand = "GMT+05:00-+05-Asia/Samarkand"
		GMT_05_00__05_Asia_Tashkent = "GMT+05:00-+05-Asia/Tashkent"
		GMT_02_00_CEST_Europe_Vatican = "GMT+02:00-CEST-Europe/Vatican"
		GMT_04_00_AST_America_St_Vincent = "GMT-04:00-AST-America/St_Vincent"
		GMT_04_00_VET_America_Caracas = "GMT-04:00-VET-America/Caracas"
		GMT_04_00_AST_America_Tortola = "GMT-04:00-AST-America/Tortola"
		GMT_04_00_AST_America_St_Thomas = "GMT-04:00-AST-America/St_Thomas"
		GMT_07_00_ICT_Asia_Ho_Chi_Minh = "GMT+07:00-ICT-Asia/Ho_Chi_Minh"
		GMT_11_00_VUT_Pacific_Efate = "GMT+11:00-VUT-Pacific/Efate"
		GMT_12_00_WFT_Pacific_Wallis = "GMT+12:00-WFT-Pacific/Wallis"
		GMT_13_00_WSST_Pacific_Apia = "GMT+13:00-WSST-Pacific/Apia"
		GMT_03_00_AST_Asia_Aden = "GMT+03:00-AST-Asia/Aden"
		GMT_03_00_EAT_Indian_Mayotte = "GMT+03:00-EAT-Indian/Mayotte"
		GMT_02_00_SAST_Africa_Johannesburg = "GMT+02:00-SAST-Africa/Johannesburg"
		GMT_02_00_CAT_Africa_Lusaka = "GMT+02:00-CAT-Africa/Lusaka"
		GMT_02_00_CAT_Africa_Harare = "GMT+02:00-CAT-Africa/Harare"

	class Useproxyport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Securecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpcip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Aftpallowrandomsourceport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cookieversion:
		_0 = "0"
		_1 = "1"

	class Internaluserlogin:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsparam_response(base_response) :
	def __init__(self, length=1) :
		self.nsparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsparam = [nsparam() for _ in range(length)]

