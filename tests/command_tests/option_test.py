option_data = {
	"uri"        : "v2/iaas/virtual-machines",
	"description": "",
	"directories": [
		".",
		"..",
		"meta-data",
		"{vm}",
		"templates",
		"snapshots",
		"wizards",
		"overview"
	],
	"methods"    : {
		"GET" : {
			"list": {
				"uri"           : "v2/iaas/virtual-machines",
				"description"   : None,
				"search"        : {
					"uri"       : "v2/iaas/virtual-machines",
					"parameters": [
						{
							"name"       : "datacenterNode",
							"type"       : "string",
							"description": ""
						},
						{
							"name"       : "name",
							"type"       : "string",
							"description": ""
						},
						{
							"name"       : "tags",
							"type"       : "$tags",
							"description": ""
						},
						{
							"name"       : "status",
							"type"       : "string",
							"description": ""
						},
						{
							"name"       : "uuid",
							"type"       : "string",
							"description": ""
						},
						{
							"name"       : "haPriority",
							"type"       : "int",
							"description": ""
						},
						{
							"name"       : "snapshots",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "templates",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "defaultTemplates",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "losts",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "locked",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "passive",
							"type"       : None
							,
							"description": ""
						},
						{
							"name"       : "ipAddr",
							"type"       : "string",
							"description": ""
						}
					]
				},
				"returns"       : "json|array",
				"authentication": "required"
			}
		},
		"POST": {
			"fields": [
				{
					"name"               : "required|max:150",
					"hostname"           : "max:150",
					"total_cpu"          : "required|integer|min:1|max:32",
					"total_ram"          : "required|integer|min:512|max:524288",
					"description"        : "max:500",
					"datacenter_node_ref": "required|exists:datacenter_nodes,id_ref",
					"compute_member_ref" : "nullable|exists:compute_members,id_ref"
				}
			]
		}
	}
}
