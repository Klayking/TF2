#include <sourcemod> //imports sourcemod functions

/**
 * This plugin is aiming to:
 * Post an announcement in chat at regular intervals
 * With:
 * Custom Intervals
 * Custom Messsage
 */

// public function that declares all info where Plugin is the class/struct
public Plugin:myinfo =
{
	name = "Unfinnished TF2CSA Timed Announcer",
	author = "Zoidberg",
	description = "Plugin for TF2CSA, and the Trinity Trade Server",
	version = "0.1",
	url = "http://184.22.121.73/"
};

/*
 * Global variables
 **/
	new String:Message[1024] = "Zoid's Announcement Plugin Successfully Loaded.";
	new Interval = 30;
	new Stopped=0;
 
public OnPluginStart()
{
	PrintToServer("Zoid's Announcement Plugin Successfully Loaded.");
	RegConsoleCmd("sm_Message", Command_Message, "Sets the message for the announcement.");
	RegConsoleCmd("sm_Interval", Command_Interval, "Sets interval between announcements, in seconds.");
	RegConsoleCmd("sm_StartMessages", Command_StartMessages, "Starts Timer again.");
	RegConsoleCmd("sm_StopMessages", Command_StopMessages, "Stops Timer.");
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
	new String:arg[1024];
	new String:full[256];

	GetCmdArgString(arg,1024);
	
	PrintToChatAll("Interval changed to" + arg);
	Interval = StringToInt(arg[0]);
	
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