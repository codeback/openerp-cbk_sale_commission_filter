# -*- encoding: utf-8 -*-
##############################################################################
#
#    res_partner
#    Copyright (c) 2013 Codeback Software S.L. (http://codeback.es)    
#    @author: Miguel García <miguel@codeback.es>
#    @author: Javier Fuentes <javier@codeback.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
from datetime import datetime, timedelta
from openerp.tools.translate import _

import pdb

class sale_order(osv.osv):
    """añadimos los nuevos campos"""

    _inherit = "sale.order"

    def _get_agent(self, cr, uid, ids, field_names, arg, context=None):
        """
        Gets information from related models for updating purposes       
        """                    
        vals={}
        for so in self.browse(cr,uid,ids, context=context):          
          
            if so.sale_agent_ids and len(so.sale_agent_ids) > 0:
                vals[so.id] = so.sale_agent_ids[0].agent_id.id
            else:
                vals[so.id] = None

        return vals

    _columns = {   
        'sale_agent_id': fields.function(_get_agent,
                          string=u'Agente',
                          type='many2one',
                          relation='sale.agent',                          
                          store=True)
    }

