import user.authentication
import transactions.journal
# import banking.reconciliation
# import banking.fvb.reconciliation
# import banking.ubsa.reconciliation
import sys
import banking
# import banking.online.reconciliation


if __name__ == "__main__":

    if (len(sys.argv) != 0):
        i = 0
        for i in range(len(sys.argv)):
            if i > 0:
                print(sys.argv[i])
            i += 1

    user.authentication.authenticate_user()
    
    transactions.journal.receive_income(100)

    transactions.journal.pay_expense(100)
    
    banking.do_reconciliation()

    # banking.reconciliation.do_reconciliation()

    # banking.fvb.reconciliation.do_reconciliation()

    # banking.ubsa.reconciliation.do_reconciliation()

    # banking.online.reconciliation.do_reconciliation()
