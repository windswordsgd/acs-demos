package org.gardler.biglittlechallenge.olympics;

import java.util.ArrayList;
import java.util.List;

import org.gardler.biglittlechallenge.olympics.ai.DumbPlayer;
import org.gardler.biglittlechallenge.olympics.model.Player;
import org.gardler.biglittlechallenge.olympics.tournament.Tournament;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * This is the main application class. We run this to start a game.
 *
 */
public class App 
{
	
	private static Logger logger = LoggerFactory.getLogger(App.class);
        
    public static void main( String[] args )
    {
        logger.debug("Starting the Olympics card game.");
        
    	List<Player> players = new ArrayList<Player>();
    	players.add(new DumbPlayer("AI Player One"));
    	players.add(new DumbPlayer("AI Player Two"));
    	players.add(new DumbPlayer("AI Player Three"));
    	players.add(new DumbPlayer("AI Player Four"));
    	players.add(new DumbPlayer("AI Player Five"));
    	
    	Tournament tournament = new Tournament(players);
    	tournament.start();
    }


}