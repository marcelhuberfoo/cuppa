
#          Copyright Jamie Allsop 2016
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

#-------------------------------------------------------------------------------
#   CopyFilesMethod
#-------------------------------------------------------------------------------

import cuppa.progress


class CopyFilesMethod:

    def __call__( self, env, target, source ):
        installed_files = env.Install( target, source )
        cuppa.progress.NotifyProgress.add( env, installed_files )
        return installed_files

    @classmethod
    def add_to_env( cls, cuppa_env ):
        cuppa_env.add_method( "CopyFiles", cls() )

