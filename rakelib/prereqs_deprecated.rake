# prereqs tasks deprecated to paver

require 'colorize'

def deprecated(deprecated, deprecated_by)

    task deprecated do

        puts("Task #{deprecated} has been deprecated. Use #{deprecated_by} instead.".red)
        sh(deprecated_by)
        exit
    end
end

deprecated('install_prereqs','paver install_prereqs')
deprecated('install_node_prereqs','paver install_node_prereqs')
deprecated('install_ruby_prereqs','paver install_ruby_prereqs')
deprecated('install_python_prereqs','paver install_python_prereqs')

