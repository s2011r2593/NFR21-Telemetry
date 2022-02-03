
def responseToMessage(message, watchdog):
    match message.split():
        case ["BARKBARK"]:
            return watchdog.bark();
        case ["LIST_SENSORS_BY_SUBTEAM"]:
            return list_sensors_by_subteam()
        case ["VALS", *sensorIDs]: 
            rFrame = watchdog.mostRecentFrame()
            return {sensorID : rFrame[sensorID] for sensorID in sensorIDs}
                
        case ["STATUS"]:
                ## TODO
            return ":)"
        #case ["SWITCH_SOURCE", newstate]:
        #    if historic.set_state(self, newstate):
        #        return ":)"
        #    else:
        #        return ":("

        case ["LIST_HISTORIC_DATAFILES"]:
            #if self.cloud:
            #       ## Awaiting Cloud API
            #   return ":("
            #else:
            #    path = "" # GET THE PATH SOMEHOW
            #    files = historic.list_data_files(path)
            #    if files:
            #        return files
            #    else:
            #        return ":("
            return [["name1", 420], ["name2", 69]]

        case ["REQUEST_HISTORIC_DATAFILE_BY_TIME", timestamp]:
            if self.cloud:
                ## Awaiting Cloud API
                return ":("
            else:
                path = "" # GET THE PATH SOMEHOW
                files = historic.find_files_by_dt(path, timestamp)
                if files:
                    if len(files) > 0:
                        return files
                    else:
                        return "FILE NOT FOUND"
                else:
                    return ":("

        case ["REQUEST_HISTORIC_DATAFILE_BY_NAME", name]:
            ## Awaiting Cloud API
            return "no lol"
        case ["END_SESSION", name]:
            ## TODO NAME DATA FILE
            watchdog.kill()
            return ":)"
        case ["BEGIN_SESSION"]:
            if watchdog.timeToDie.set():
                return "SESSION ALREADY ACTIVE"
            else:
                watchdog.observe()
                return "SESSION STARTED"
        case _:
            return None
            
