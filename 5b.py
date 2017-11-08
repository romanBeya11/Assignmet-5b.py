'''
Created by Roman Beya
Created on 6-nov-2017
Created for ICS3U
This program plays Black Jack!
'''
from numpy import random
import ui

# generating random cards for dealer(2) and player(3)
dealer_card_1 = random.randint(1, 11)
dealer_card_2 = random.randint(1, 11)
player_card_1 = random.randint(1, 11)
player_card_2 = random.randint(1, 11)

# Generated if they request a 3rd card
player_card_3 = random.randint(1, 11)

# creating the variables which hold the sum of each opponents cards, globally
dealer_cards_sum = 0
player_cards_sum = 0

def view_cards_touch_up_inside(sender):
	# When the user presses this button, their cards will appear
	
	# calling global variables to be manipulated
	global player_card_1
	global player_card_2
	
	# Displaying player cards
	view['player_card_label'].text = "My cards: {0}, {1}".format(player_card_1, player_card_2)
	
	# disable button if pressed
	view['view_cards_button'].enabled = False
	view['view_cards_button'].alpha = 0.25
	
			
def draw_card_touch_up_inside(sender):
	# if the user draws another card, this function will serve as a relay 
	# This function serves to send the 'check cards' function that a new card is being drawn	
	global player_card_1
	global player_card_2
	global player_card_3
	
	# display new card
	view['player_card_label'].text = 'My Cards: {0}, {1}, {2}'.format(player_card_1, player_card_2, 				player_card_3)
	
	# disable this button if it is pressed
	view['draw_cards_button'].enabled = False
	view['draw_cards_button'].alpha = 0.25
	
	
def check_cards_touch_up_inside(sender):
	# compares the sum of dealers cards vs sum of player cards
	
	# call global variables to be manipulated
	global dealer_card_1
	global dealer_card_2
	global player_card_1
	global player_card_2
	global player_card_3
	global dealer_cards_sum
	global player_cards_sum
	
	# display the dealers cards
	view['dealer_card_label'].text = "Dealer's Cards:\n{0}, {1}".format(dealer_card_1, dealer_card_2)
	
	# checking if the draw card button is disable implies that it has been pressed
	# Thus, a new card can now be generated
	if view['draw_cards_button'].enabled == False:
		# display new card
		view['player_card_label'].text = 'My Cards: {0}, {1}, {2}'.format(player_card_1, player_card_2, 				player_card_3)
		
		# summing each opponents cards to determine who is closer to 21
		dealer_cards_sum = dealer_card_1 + dealer_card_2
		player_cards_sum = player_card_1 + player_card_2 + player_card_3
		
		# comparing their respective sums
		if dealer_cards_sum >= player_cards_sum and dealer_cards_sum <= 21:
			# This condition will only run if the dealer is currently winning
			
			view['output_label'].text = "Sum of Dealer's Cards: {0}\nSum of Your Cards: {1}\nYou Lose.".format(dealer_cards_sum, player_cards_sum)
		else:
			# If the condition tested above is proven false, then that implies that the player is currently winning
			if player_cards_sum <= 21:
				view['output_label'].text = "Sum of Dealer's Cards: {0}\nSum of Your Cards: {1}\nYou Win!".format(dealer_cards_sum, player_cards_sum)
	else:
			# If the user chooses not to draw another card...
			# summing each opponents cards to determine who is closer to 21
			dealer_cards_sum = dealer_card_1 + dealer_card_2
			player_cards_sum = player_card_1 + player_card_2
		
			# comparing their respective sums
			if dealer_cards_sum >= player_cards_sum and dealer_cards_sum <= 21:
				# This condition will only run if the dealer is currently winning
				
				view['output_label'].text = "Sum of Dealer's Cards: {0}\nSum of Your Cards: {1}\nYou Lose.".format(dealer_cards_sum, player_cards_sum)
			else:
				# If the condition tested above is proven false, then that implies that the player is currently winning
				if player_cards_sum <= 21:
					view['output_label'].text = "Sum of Dealer's Cards: {0}\nSum of Your Cards: {1}\nYou Win!".format(dealer_cards_sum, player_cards_sum)
					
				# if the user choose not the draw another card, disable the button once they have checked their cards against the dealer
				view['draw_cards_button'].enabled = False
				view['draw_cards_button'].alpha = 0.25
				
	# disable this button if it is pressed
	view['check_cards_button'].enabled = False
	view['check_cards_button'].alpha = 0.25
					
view = ui.load_view()
view.present('full_screen')
