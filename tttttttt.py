

def htmlA5():
    return '''
    <td align="center" valign="top" height="100%%" width="100%%" bgcolor="grey">
                565565%s%s%s
                ''' % ('333', '333', '333')


def htmlA():
    return '''
                <td align="center" valign="top" height="100%" width="100%" bgcolor="grey">
                    <table cellpadding="0" cellspacing="0" height="100%" width="392">
                        <tr height="25%" bgcolor="red">
                            <td align="left" valign="top" bgcolor="blue">
                                <p><big><big>%s</big></big>
                            </td>
                        </tr>
                        <tr height="33%" bgcolor="red">
                            <td align="center" valign="top" bgcolor="green">
                                <p><big><big><big>%s</big></big></big><br>
                                <p><big>%s</big>
                            </td>
                        </tr>
                        <tr  bgcolor="red">
                            <td align="center" valign="top" bgcolor="blue">
                                <p><big>Новосибирск 2030</big>
                            </td>
                        </tr>
                    </table>
                </td> 
                ''' % ('333', '333', '333')

rr=htmlA5()
print(rr)
