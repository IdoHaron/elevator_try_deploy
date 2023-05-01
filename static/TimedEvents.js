class RecurringEvent{
    constructor(callback_function, time_interval, termination_function, termination_check_interval){
        this.recurring_function = callback_function
        this.recurring_timeout = time_interval
        this.termination_test_function = termination_function
        this.termination_test_timeout=  termination_check_interval
        this.#reset();
        this.setup();
    }
    termination(){
        clearInterval(this.#recurring_interval_id)
        clearInterval(this.#termination_test_interval_id )
        this.#reset()
    }
    setup(){
        if (this.is_active){
            return
        }
        this.#setup_recurring();
        this.#setup_termination();
        this.is_active = true
    }
    #test_termination(){
        if (this.termination_test_function())
            this.#termination()
    }
    #reset(){
        this.#recurring_interval_id = null
        this.#termination_test_interval_id = null
        this.is_active = false
    }
    #setup_termination(){
        if (this.termination_test_timeout > 0)
            this.#termination_test_interval_id=  setInterval(this.#test_termination, this.termination_test_timeout)
    }  
    #setup_recurring(){
        this.#recurring_interval_id = setInterval(this.recurring_function, this.recurring_timeout)
    }

}
