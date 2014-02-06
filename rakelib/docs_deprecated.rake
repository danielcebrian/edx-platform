# doc tasks deprecated to paver

require 'colorize'

def deprecated(deprecated, deprecated_by)

     task deprecated, [:type, :quiet] do |t,args|

        args.with_defaults(:quiet => "quiet")
        new_cmd = [deprecated_by]

        if args.quiet == 'verbose' and deprecated == 'builddocs'
            new_cmd << '--verbose'
        end

        if not args.type.nil?
            new_cmd << "--type=#{args.type}"
        end

        new_cmd = new_cmd.join(" ")

        puts("Task #{deprecated} has been deprecated. Use \"#{new_cmd}\" instead. Waiting 5 seconds...".red)
        sleep(5)
        sh(new_cmd)
    end

end


deprecated('builddocs','paver build_docs')
deprecated('showdocs','paver show_docs')
deprecated('doc','paver doc')
