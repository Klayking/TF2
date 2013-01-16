#include <sourcemod> //imports sourcemod functions

/**
 * This plugin is aiming to:
 * Store who is in time for a mix
 * Menu for picking players
 * 
 * Store who is late for a mixes
 * Have some function that will enable re-connecting and place keeping
 * Force Spec
 * Vote Captains
 * Vote map
 * 
 * Optionally:
 * Post announcements for mixes if:
 * Admin triggers the function
 * 4 people have joined the server
 * smurf registering
 */

 // public function that declares all info where Plugin is the class/struct
public Plugin:myinfo =
{
	name = "TF2CSA Mix Organiser",
	author = "Zoidberg",
	description = "Plugin for TF2 mixes/pick-ups",
	version = "0.1",
	url = "http://www.sourcemod.net/"
};

/*
 * Global variables
 **/
 new String:arrClients[32], String:arrOnTime[12], String:arrLate[20];

public OnPluginStart()
{
	PrintToConsole("Zoid's Mix  (Alpha Version) successfully loaded, success!")
	RegConsoleCmd("sm_OnTime", Command_OnTime, "Displays the clients that arrived in time for the mix");
	RegConsoleCmd("sm_Late", Command_Late, "Displays the clients that were late for the mix.");
}

public OnClientConnected()
{
	new Connected = getClientCount(true);
	new String:Name = getClientName();
	arrClients[Connected] = Name;
	if ( Connected < 12)
	{
		arrOnTime[Connected] = Name;
	}
	else
	{
		arrLate[Connected - 12] = Name;
	}
}

public OnClientDisconnect()
{
	new Connected = getClientCount(true);
	new String:Name = getClientName();
	arrClients[Connected] = Name;
	if ( Connected < 12)
	{
		arrOnTime[Connected] = Name;
	}
	else
	{
		arrLate[Connected - 12] = Name;
	}
}

//OnTime Command
public Action:Command_OnTime(client, args)
{
	new i = 0
	PrintToChatAll("\x011On Time:");
	new String:OnTime;
	OnTime = "";
	while ( (arrOnTime[i] != 0) && ( i < 12))
	{
		if (i == 0)
		{
			OnTime += arrOnTime[i];
		}
		else
		{
			OnTime += ", " + arrOnTime[i];
		}
	}
	PrintToChatAll(OnTime);
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}

//Late command
public Action:Command_Late(client, args)
{
	new i = 0
	PrintToChatAll("\x011Late:");
	new String:Late;
	Late = "";
	while ( (arrLate[i] != 0) && ( i < 12))
	{
		if (i == 0)
		{
			Late += arrLate[i];
		}
		else
		{
			Late += ", " + arrLate[i];
		}
	}
	PrintToChatAll(Late);
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}