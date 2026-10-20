---
type: topic
subject: AttExam
status: not-started
frequency: every-paper
tags:
  - attexam/topic
---

# Correspondent Accounting, Conveyancing Statements and VAT

Tested in **every Part 4 (Legal Practitioners' Bookkeeping)** sitting as two major practical questions (typically 25–50 marks each): (1) recording a **property transfer / conveyancing transaction** from buyer deposit and bank guarantee through registration and final accounting statement, and (2) recording **instructing vs correspondent attorney** collections, fees, and 1/3 allowance splits.

> [!important] Statutory Update (Current Law vs Historical Memos)
> - **VAT Rate**: **15%** since 1 April 2018 (memos from 2015 to Feb 2018 use **14%**). Always check the exam sitting date or instruction: for current sittings, VAT on fees (`excl. VAT × 15%`) or extracting VAT from a VAT-inclusive fee (`incl. VAT × 15 / 115`) uses **15%**.
> - **Compulsory VAT Registration Threshold**: Annual taxable supplies (fee income) exceeding **R1 000 000** in any 12-month period (`AttExam 2019-08-22 P4` Q3.1).

## 1. Conveyancing / Property Transfer Accounting (30–50 marks)

When acting as the conveyancer for the Seller (or recording the Purchaser's ledger):
1. **Receipts into Trust (`Dr Trust Cash Book / Cr Purchaser (T)`)**:
   - Cash deposit paid by Purchaser.
   - Transfer costs and Transfer Duty paid in by Purchaser.
   - If the deposit is invested in a **s86(4) (formerly s78(2A))** account pending registration:
     - On investment: `Dr s86(4) Investment / Cr Trust Cash Book`.
     - On maturity at registration: `Dr Trust Cash Book / Cr s86(4) Investment (capital)` and `Cr Purchaser (T) (interest)` (less 5% LPFF levy under s86(5) where applicable).
   - Proceeds of the **Bank Guarantee** paid in on date of registration (`Dr Trust Cash Book / Cr Purchaser (T)`).
2. **Disbursements & Fees**:
   - **Transfer Duty to SARS**: Paid either from Trust (`Cr Trust Cash Book / Dr Purchaser (T)`) if trust funds were deposited for it, or from Business (`Cr Business Cash Book / Dr Purchaser (B)`) if advanced or after transfer.
   - **Conveyancing & Bond Fees**: Debited in the **Business Ledger** via the **Fees Journal** (`Dr Purchaser (B) / Cr Fees & Cr Output VAT`).
   - **Transfer from Trust to Business**: Transfer the exact amount of fees + VAT + business disbursements (`Dr Purchaser (T) / Cr Purchaser (B)` in the Transfer Journal, and `Cr Trust Cash Book / Dr Business Cash Book`).
3. **Final Payouts on Registration (`Cr Trust Cash Book / Dr Purchaser (T)`)**:
   - Pay the net purchase price to the **Seller** (or settle existing mortgage bond + balance to Seller).
   - Refund the **s86(4) interest** (and any unused cost refund) to the **Purchaser**.
4. **Accounting Statement to Client**:
   - Two-column statement (`Debits` vs `Credits`) showing all monies received (deposit, guarantees, costs deposit, investment interest) balanced against all payments made (purchase price to seller, transfer duty, conveyancer's fees, VAT, and final refund cheque/EFT). Both columns must balance to the cent!

## 2. Instructing vs Correspondent Attorney Accounting (25–45 marks)

Always identify first whether you are the **Instructing Attorney** (where the client sits) or the **Correspondent / Instructed Attorney** (at the seat of the court):

### A. When You Are the Instructing Attorney (e.g., `AttExam 2017-08-23 P4` Q2)
- Correspondent collects debt from debtor and remits net cheque/EFT after deducting their fees & disbursements (less your 1/3 allowance):
  1. **Record full collection in Trust Journal**: `Dr Correspondent (T) / Cr Client (T)` with the **full capital collected**.
  2. **Record correspondent's gross charge to client in Trust Journal**: `Dr Client (T) / Cr Correspondent (T)` with the **full fees + disbursements + VAT** charged by the correspondent to the client.
  3. **Record your 1/3 fee allowance in Fees Journal (Business)**: `Dr Correspondent (B) / Cr Fees & Cr Output VAT` with your **1/3 allowance** (plus VAT).
  4. **Record receipt of correspondent's remittance in Trust Cash Book**: `Dr Trust Cash Book / Cr Correspondent (T)`.
  5. **Transfer your 1/3 allowance from Trust to Business**: `Dr Correspondent (T) / Cr Correspondent (B)` (Transfer Journal) and `Cr Trust Cash Book / Dr Business Cash Book`.
  6. **Pay net balance to Client from Trust Cash Book**: `Dr Client (T) / Cr Trust Cash Book`.

### B. When You Are the Correspondent (Instructed Attorney) (e.g., `AttExam 2016-02-10 P4` Q1, `AttExam 2018-02-07 P4` Q1)
- You act on instructions from the Instructing Attorney ("Correspondent" is your client in your books):
  1. **Collection received from debtor**: `Dr Trust Cash Book / Cr Correspondent (T)`.
  2. **Disbursements paid (Sheriff, Counsel, Expert)**: Paid from Business Cash Book (`Dr Correspondent (B) / Cr Business Cash Book`) unless trust funds are held specifically for that disbursement.
  3. **Raise gross fees in Business Journal**: `Dr Correspondent (B) / Cr Fees & Cr Output VAT`.
  4. **Grant 1/3 (or agreed) allowance to Instructing Attorney in Business Journal**: `Dr Fees & Dr Output VAT / Cr Correspondent (B)`.
  5. **Transfer net amount owed to you from Trust to Business**: `Dr Correspondent (T) / Cr Correspondent (B)` and `Cr Trust Cash Book / Dr Business Cash Book`.
  6. **Remit remaining balance to Instructing Attorney**: `Dr Correspondent (T) / Cr Trust Cash Book`.

## Seen in past papers

- [[AttExam 2017-02-15 P4]] — Q3 (50 marks: Purchaser conveyancing ledger + s78(2A) Phoenix Bank + Correspondent allowance + Transfer of Property statement)
- [[AttExam 2017-08-23 P4]] — Q2 (30 marks: Instructing attorney recording correspondent collection & ½ allowance), Q3 (25 marks: David trust registration, revenue stamps, fees & accounting statement)
- [[AttExam 2019-03-07 P4]] — Q3 (30 marks: Patricia trust deposit, financial adviser disbursement, fees @ 15% VAT, transfer & accounting statement)
- [[Attorneys Exam/Official Memoranda 2015-2021/AttExam10Feb2016P4A|AttExam 2016-02-10 P4]] — Q1 (40 marks: Acting as correspondent for Minnie, 1/3 allowance entries)
- [[Attorneys Exam/Official Memoranda 2015-2021/AttExam7Feb2018P4A|AttExam 2018-02-07 P4]] — Q1 (45 marks: Correspondent ledger, counsel/expert disbursements, 1/3 allowance & statement), Q2 (40 marks: Stevens & Ben conveyancing + collection)

## Related topics

[[Trust and Business Accounting, Transfers and Reconciliations]] · [[Costs, Tenders and Withdrawal of Action]] · [[Professional Ethics and Conduct]]
