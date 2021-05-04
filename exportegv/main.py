from meerk40t.device.lasercommandconstants import *

output_path = "/home/jacob/cut/output.egv"

def plugin(kernel, lifecycle):
    if lifecycle == 'register':
        """
        Register our changes to meerk40t. These should modify the registered values within meerk40t or install different
        modules and modifiers to be used in meerk40t.
        """

        def planexport():
            def export():
                context = kernel.get_context("/")
                context("egv_export {}\n".format(output_path))
                context("window close Controller\n")
                context("window close JobSpooler\n")
                context("abort\n")
            yield COMMAND_FUNCTION, export
        kernel.register('plan/export', planexport)

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
        """
        context = kernel.get_context("/")
        elements = context.elements

        @elements.tree_operation("Export EGV", node_type="root", help="Shortcut to export output.egv. Resets controller.")
        def run_job(node, **kwargs):
            context("plan clear\n")
            context("plan copy\n")
            context("plan preprocess\n")
            context("plan validate\n")
            context("plan blob\n")
            context("plan preopt\n")
            context("plan optimize\n")
            context("plan command --op export\n")
#            context("plan command --op interrupt\n")
            context("window open Controller\n")
            context("window open JobSpooler\n")
            context("start\n")
            context("hold\n")
            context("plan spool\n")

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
