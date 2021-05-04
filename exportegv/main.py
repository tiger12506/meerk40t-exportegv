
def plugin(kernel, lifecycle):
    if lifecycle == 'register':
        """
        Register our changes to meerk40t. These should modify the registered values within meerk40t or install different
        modules and modifiers to be used in meerk40t.
        """

        @kernel.console_command('example', help="Says Hello World.")
        def example_cmd(command, channel, _, args=tuple(), **kwargs):
            channel(_('Hello World'))
    elif lifecycle == 'boot':
        """
        Do some persistent actions or start modules and modifiers. Register any scheduled tasks or threads that need
        to be running for our plugin to work. 
        """
        pass
    elif lifecycle == 'ready':
        """
        Start process running. Sometimes not all modules and modifiers will be ready as they are processed in order
        during boot. If your thread or work depends on other parts of the system being fully established they should 
        work here.

        Try out:
        def interrupt():
            yield COMMAND_WAIT_FINISH
            def intr():
                input("waiting for user...")
            yield COMMAND_FUNCTION,intr
        kernel.register("plan/interrupt", self.interrupt)
        """
        context = kernel.get_context("/")
        elements = context.elements

        @elements.tree_operation("Hold and Spool Job", node_type="root", help="Shortcut to start and spool entire job")
        def run_job(node, **kwargs):
            context.console("plan clear\n")
            context.console("plan copy\n")
            context.console("plan preprocess\n")
            context.console("plan validate\n")
            context.console("plan blob\n")
            context.console("plan preopt\n")
            context.console("plan optimize\n")
            context.console("window open Controller\n")
            context.console("start\n")
            context.console("hold\n")
            context.console("plan spool\n")

        @elements.tree_operation("Export EGV", node_type="root", help="Shortcut to export output.egv. Resets controller.")
        def exportegv(node, **kwargs):
            context.console("egv_export /home/jacob/cut/output.egv\n")
            context.console("abort\n")
            context.console("timer 1 10 window close Controller\n")
    elif lifecycle == 'mainloop':
        """
        This is the start of the gui and will capture the default thread as gui thread. If we are writing a new gui
        system and we need this thread to do our work. It should be captured here. This is the main work of the program. 
        """
        pass
    elif lifecycle == 'shutdown':
        """
        Meerk40t's closing down, our plugin should adjust accordingly. All registered meerk40t processes will be stopped
        any plugin processes should also be stopped so the program can close correctly.
        """
        pass
