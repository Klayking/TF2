"Resource/UI/HudDamageAccount.res"
{
	 "CDamageAccountPanel"
    {
        "fieldName"                "CDamageAccountPanel"
        "text_x"                "0"
        "text_y"                "0"
        "delta_item_end_y"        "0"
        "PositiveColor"            "255 255 0 255"
        "NegativeColor"            "255 255 0 255"
        "delta_lifetime"        "1.5"
        "delta_item_font"        "HudFontMedium"
        "delta_item_font_big"    "HudFontMedium"
    }

	"DamageAccountValue"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"DamageAccountValue"
		"xpos"			"c-50"
		"ypos"			"r180" //"r146"
		"zpos"			"2"
		"wide"			"100"
		"tall"			"31"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%metal%"
		"delta_lifetime"		"10.0"
		"textAlignment"	"center"
		"fgcolor"		"menuOrange"
		"font"			"HudFontGiant"
	}

	"DamageAccountValueShadow"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"DamageAccountValueShadow"
		"xpos"			"c-49"
		"ypos"			"r179"
		"zpos"			"1"
		"wide"			"100"
		"tall"			"31"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%metal%"
		"delta_lifetime"		"10.0"
		"textAlignment"	"center"
		"fgcolor"		"Black"
		"font"			"HudFontGiant"
	}
}