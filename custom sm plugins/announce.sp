#include <sourcemod> //imports sourcemod functions

/**
 * This plugin is aiming to:
 * Post an announcement in chat at regular intervals
 * With:
 * Custom Intervals
 * Custom Messsage
 * 
 * Fixes:
 * 0.2 Fixed Exploit with commands being available to admins only now
 * 0.3 Fixed sm_interval not changing the interval
 */

// public function that declares all info where Plugin is the class/struct
public Plugin:myinfo =
{
	name = "Unfinnished TF2CSA Timed Announcer",
	author = "Zoidberg",
	description = "Plugin for TF2CSA, and the Trinity Trade Server",
	version = "0.3",
	url = "http://184.22.121.73/"
};

/*
 * Global variables
 **/
	new String:Message[1024] = "Zoid's Announcement Plugin Successfully Loaded.";
	new Float:Interval = 30.0;
	new Stopped=0;
	
public OnPluginStart()
{
	PrintToServer("Zoid's Announcement Plugin Successfully Loaded.");
	RegAdminCmd("sm_message", Command_Message, ADMFLAG_GENERIC,  "Sets the message for the announcement.");
	RegAdminCmd("sm_interval", Command_Interval, ADMFLAG_GENERIC,  "Sets interval between announcements, in seconds.");
	RegAdminCmd("sm_startmessages", Command_StartMessages, ADMFLAG_GENERIC,  "Starts Timer again.");
	RegAdminCmd("sm_stopmessages", Command_StopMessages, ADMFLAG_GENERIC,  "Stops Timer.");
	TimerOn();
}

public TimerOn()
{
	CreateTimer(Interval, Timer_PrintMessage, _, TIMER_REPEAT);	
	PrintToChatAll("Announcements switched On");
}

//Start Timer
public Action:Command_StartMessages(client, args)
{
	TimerOn();
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}
//Stop Timer
public Action:Command_StopMessages(client, args)
{
	
	PrintToChatAll("Announcements switched Off");
	Stopped = 1;
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}

//Message Command
public Action:Command_Message(client, args)
{
	new String:full[1024];
	
	GetCmdArgString(full, sizeof(full));

	Message = full;
	
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}

//Interval command
public Action:Command_Interval(client, args)
{
	new String:arg[20];
	GetCmdArgString(arg, sizeof(arg));
	Interval = StringToFloat(arg);
	PrintToChatAll("Interval changed to %i", RoundFloat(Interval));
	KillTimer(Timer_PrintMessage)
	CreateTimer(Interval, Timer_PrintMessage, _, TIMER_REPEAT);	
	
	return Plugin_Handled; // This always needs to be included at the end of an action, also stops function
}
 
public Action:Timer_PrintMessage(Handle:timer)
{
	// Create a global variable visible only in the local scope (this function).

	if (Stopped == 1) {
		return Plugin_Stop;
	}
	PrintToChatAll(Message);
	return Plugin_Continue;
}