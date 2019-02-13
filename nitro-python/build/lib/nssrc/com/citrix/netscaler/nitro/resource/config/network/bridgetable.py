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

class bridgetable(base_resource) :
	""" Configuration for bridge table entry resource. """
	def __init__(self) :
		self._bridgeage = None
		self._nodeid = None
		self._vlan = None
		self._ifnum = None
		self._vxlan = None
		self._mac = None
		self._vtep = None
		self._flags = None
		self._channel = None
		self.___count = None

	@property
	def bridgeage(self) :
		r"""Time-out value for the bridge table entries, in seconds. The new value applies only to the entries that are dynamically learned after the new value is set. Previously existing bridge table entries expire after the previously configured time-out value.<br/>Default value: 300<br/>Minimum length =  60<br/>Maximum length =  300.
		"""
		try :
			return self._bridgeage
		except Exception as e:
			raise e

	@bridgeage.setter
	def bridgeage(self, bridgeage) :
		r"""Time-out value for the bridge table entries, in seconds. The new value applies only to the entries that are dynamically learned after the new value is set. Previously existing bridge table entries expire after the previously configured time-out value.<br/>Default value: 300<br/>Minimum length =  60<br/>Maximum length =  300
		"""
		try :
			self._bridgeage = bridgeage
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""VLAN  whose entries are to be removed.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""VLAN  whose entries are to be removed.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		r"""INTERFACE  whose entries are to be removed.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""INTERFACE  whose entries are to be removed.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""VXLAN  whose entries are to be removed.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""VXLAN  whose entries are to be removed.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def mac(self) :
		r"""The MAC address of the target.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@property
	def vtep(self) :
		r"""The IP address of the VTEP.
		"""
		try :
			return self._vtep
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Display flags,.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def channel(self) :
		r"""The Tunnel through which bridge entry is learned.
		"""
		try :
			return self._channel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bridgetable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bridgetable
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
		r""" Use this API to update bridgetable.
		"""
		try :
			if type(resource) is not list :
				updateresource = bridgetable()
				updateresource.bridgeage = resource.bridgeage
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ bridgetable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].bridgeage = resource[i].bridgeage
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of bridgetable resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = bridgetable()
				return unsetresource.unset_resource(client, args)
			else :
				if (resource and len(resource) > 0) :
					unsetresources = [ bridgetable() for _ in range(len(resource))]
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear bridgetable.
		"""
		try :
			if type(resource) is not list :
				clearresource = bridgetable()
				clearresource.vlan = resource.vlan
				clearresource.ifnum = resource.ifnum
				clearresource.vxlan = resource.vxlan
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ bridgetable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].vlan = resource[i].vlan
						clearresources[i].ifnum = resource[i].ifnum
						clearresources[i].vxlan = resource[i].vxlan
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the bridgetable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = bridgetable()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the bridgetable resources that are configured on netscaler.
	# This uses bridgetable_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = bridgetable()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of bridgetable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bridgetable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the bridgetable resources configured on NetScaler.
		"""
		try :
			obj = bridgetable()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of bridgetable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bridgetable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class bridgetable_response(base_response) :
	def __init__(self, length=1) :
		self.bridgetable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bridgetable = [bridgetable() for _ in range(length)]

