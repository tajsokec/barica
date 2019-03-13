from transitions import Machine

from chatterbot import ChatBot

import argparse

import sys

from dictionary import *
d = dictionary()

class FiniteStateMachine:
    
    states = ['listen', 'yes', 'foi_generally', 'which_classroom', 'classroom', 'which_professor',
              'professor', 'which_kind_of_study', 'which_year_of_study', 'which_group', 'schedule']

    def __init__(self):

        # Initialize the state machine
        self.machine = Machine(model=self, states=FiniteStateMachine.states, initial='listen')
        
        # Add transitions (trigger, source_state, destination_state)
        self.machine.add_transition('barice_input', 'listen', 'yes')
        
        self.machine.add_transition('foi_input', 'yes', 'foi_generally', after='foi_generally_output')
        
        self.machine.add_transition('classroom_input', 'yes', 'which_classroom')
        self.machine.add_transition('classroomN_input', 'which_classroom', 'classroom', after='classroom_output')
        
        self.machine.add_transition('professor_input', 'yes', 'which_professor')
        self.machine.add_transition('professorN_input', 'which_professor', 'professor', after='professor_output')
        
        self.machine.add_transition('schedule_input', 'yes', 'which_kind_of_study')
        self.machine.add_transition('kind_of_study_input', 'which_kind_of_study', 'which_year_of_study')
        self.machine.add_transition('year_of_study_input', 'which_year_of_study', 'which_group')
        self.machine.add_transition('groupN_input', 'which_group', 'schedule', after='schedule_output')

        self.machine.add_transition('listen_input', '*', 'listen')

    def foi_generally_output(self):
        self.listen_input()

    def classroom_output(self):
        self.listen_input()

    def professor_output(self):
        self.listen_input()

    def schedule_output(self):
        self.listen_input()

def main_branch(SENTENCE):
    CMD = chatbot.get_response( SENTENCE )
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])
    elif CMD in d['FOI']:
        m.foi_input()
        print(d['FOI'][CMD])
    elif CMD in d['Dvorana']:
        m.classroom_input()
        print(d['Dvorana'][CMD])
    elif CMD in d['Profesor']:
        m.professor_input()
        print(d['Profesor'][CMD])
    elif CMD in d['Raspored']:
        m.schedule_input()       
        print(d['Raspored'][CMD])
    else: return False

def classroom_branch(SENTENCE):
    CMD = chatbotClassroom.get_response( SENTENCE )
    if CMD in d['Classrooms']:
        m.classroomN_input()
        print(d['Classrooms'][CMD])
    else: return False
    
def professor_branch(SENTENCE):
    CMD = chatbotProfessor.get_response( SENTENCE )
    if CMD == 'Profesor Zlatko Stapić nalazi se ..':
        m.professorN_input()
        print(CMD)
    else: return False

def schedule_branch(SENTENCE):
    CMD = chatbotSchedule.get_response( SENTENCE )
    if CMD == 'Za koju godinu studija trebaš raspored?':
        m.kind_of_study_input()
        print(CMD)
    elif CMD == 'Za koji grupu trebaš raspored?':
        m.year_of_study_input()
        print(CMD)
    elif CMD == 'Izvoli raspored..':
        m.groupN_input()
        print(CMD)
    else: return False

def err_handler(SENTENCE):
    if SENTENCE == 'exit':
        sys.exit()
    else: print ('Ponovi unos molim')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( "--train", const=True, nargs='?', type=bool, help="Specify if the agent shoud be trained. If not specified agent will be started in default (listening) mode.")
    args = parser.parse_args()

    TRAIN = bool( args.train )

    chatbot = ChatBot( 'BARICA_HR', read_only=not TRAIN, database='db.sqlite3' )
    chatbotClassroom = ChatBot( 'BARICA_HR_CLASSROOM', read_only=not TRAIN, database='dbC.sqlite3')
    chatbotProfessor = ChatBot( 'BARICA_HR_PROFESSOR', read_only=not TRAIN, database='dbP.sqlite3' )
    chatbotSchedule= ChatBot( 'BARICA_HR_SCHEDULE', read_only=not TRAIN, database='dbS.sqlite3' )

    if TRAIN:
            from train import *
            from trainClassroom import *
            from trainProfessor import *
            from trainSchedule import *
            train( chatbot )
            trainClassroom( chatbotClassroom )
            trainProfessor( chatbotProfessor )
            trainSchedule ( chatbotSchedule ) 
            sys.exit()
    
    m = FiniteStateMachine()
    
    while True:
        
        try:        
            SENTENCE = input()
            
            if m.state == 'listen' or  m.state == 'yes':
                if main_branch(SENTENCE) == False:
                    err_handler(SENTENCE)

            elif m.state == 'which_classroom':
                 if classroom_branch(SENTENCE) == False:
                     err_handler(SENTENCE)

            elif m.state == 'which_professor':
                if professor_branch(SENTENCE) == False:
                    err_handler(SENTENCE)                                 

            elif m.state == 'which_kind_of_study' or m.state == 'which_year_of_study' or m.state == 'which_group':
                if schedule_branch(SENTENCE) == False:
                    err_handler(SENTENCE)
                
        except Exception:
            pass
            print('Ponovi unos')
            

    
        
