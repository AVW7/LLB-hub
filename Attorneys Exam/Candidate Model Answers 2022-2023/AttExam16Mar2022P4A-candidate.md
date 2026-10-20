---
date: '2026-10-19'
type: candidate-memo
tags:
- candidate-memo
- model-answers
- board-exams
- pending-verification
ai-first: true
role: candidate-answer
official: false
verification-status: pending-multi-agent-review
exam-date: '2022-03-16'
paper-number: 4
total-marks: 100
matching-question: '[[Attorneys Exam/Official Previous Papers 2015-2023/AttExam16Mar2022P4Q]]'
---

## For future agent & verification models

Candidate model answer generated on 2026-10-19 for **16 March 2022 Paper 4 (Legal Practitioners' Bookkeeping)** so other agents and models can verify it. Grounded in the official LSSA LEAD bookkeeping conventions in `Attorneys Exam/Official Memoranda 2015-2021/` (e.g. [[Attorneys Exam/Official Memoranda 2015-2021/AttExam20Oct2021P4A]], [[Attorneys Exam/Official Memoranda 2015-2021/AttExam18Mar2021P4A]], [[Attorneys Exam/Official Memoranda 2015-2021/AttExam5Nov2020P4A]]) and verified against the Scribd snippet (`https://www.scribd.com/document/1068448275/2022-03-Paper-4-March-2022-Memorandum`).

### Multi-Agent Verification Checklist
- [ ] Confirm mark allocations across Questions 1–4 sum to 100 (`51 + 24 + 12 + 13 = 100`).
- [ ] Verify Question 1 trust transfer rules, 5% LPFF deduction on s86(4) interest (s86(5) Legal Practice Act 28 of 2014 = R200 on R4 000 interest), and Output VAT calculation.
- [ ] Verify Question 2 correspondent accounting for Flash Attorneys (`R20 000` collected; `R2 915` fees/VAT/disbursements; `R805` 1/3 allowance incl. VAT; `R17 890` EFT received; `R17 085` paid to client Land Lord).
- [ ] Verify Question 3 Bank Reconciliation (`Supplementary Cash Book balance = +R8 000,00`; `Bank Statement R6 000,00 + Outstanding Deposit R2 000,00 = R8 000,00`).

# AttExam16Mar2022P4A — Candidate Model Memorandum (Pending Verification)

- **Matching question paper**: [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam16Mar2022P4Q]]
- **Coverage tracker**: [[notes/Board Exam Memo Coverage]]

---

## QUESTION 1 [51]

### Note on Accounting Treatment (for Verification Models)
- **Green Bank s86(4) Interest (Transaction 16)**: Under s86(5) of the Legal Practice Act 28 of 2014 (effective 1 November 2018), 5% of interest earned on a s86(4) trust investment (`5% × R4 000 = R200,00`) accrues to the Legal Practitioners' Fidelity Fund (LPFF) and 95% (`R3 800,00`) accrues to the client (K Hart). *(Note: Historical LSSA memos occasionally awarded full marks whether 100% or 95%/5% was shown; both are noted below).*
- **K Hart Transfer Costs (Transactions 9 & 11)**: K Hart paid R45 000,00 for transfer costs (transfer fees and transfer duty), and R22 000,00 transfer duty was paid to SARS, leaving R23 000,00 (`R20 000,00` fee + `R3 000,00` VAT @ 15%). Because the prompt does not explicitly state that registration of transfer occurred in K Hart's matter, strict conveyancing accounting retains the R23 000,00 in Trust until registration; however, if the examiner intended the R23 000,00 transfer fee to be billed and transferred at month-end, the alternative figures are shown in brackets `[Alt: with K Hart fee]`.

### 1. Books of Prime Entry (Journals & Cash Books)

#### Fee Journal
| Date/No. | Details / Narration | Dr (R) | Cr (R) |
|---|---|---|---|
| 3 | **M Carey (B)** | 1 150,00 | |
| | Fees | | 1 000,00 |
| | Output VAT (15%) | | 150,00 |
| | *Being fee for issuing summons in Carey v Rock* | | |
| 6 | **T Banks (B)** | 46 000,00 | |
| | Fees | | 40 000,00 |
| | Output VAT (15%) | | 6 000,00 |
| | *Being fee for drafting trust documents (Banks Family Trust)* | | |
| 10 | **A Keys (B)** *(if not previously debited)* | 25 875,00 | |
| | Fees | | 22 500,00 |
| | Output VAT (15%) | | 3 375,00 |
| | *Being professional fees rendered in divorce matter* | | |
| 13 | **M Carey (B)** | 1 725,00 | |
| | Fees (Collection Commission) | | 1 500,00 |
| | Output VAT (15%) | | 225,00 |
| | *Being collection commission on R100 000 part payment* | | |
| 19 | **D Johnson (B)** | 2 300,00 | |
| | Fees | | 2 000,00 |
| | Output VAT (15%) | | 300,00 |
| | *Being instruction fee in action against Minister of Police* | | |
| *[Alt 9]* | *[K Hart (B) — if transfer fees debited: Dr R23 000 / Cr Fees R20 000, Cr Output VAT R3 000]* | | |

#### Transfer Journal (Transaction 23 — Month-End Trust-to-Business Transfer)
| No. | Details / Narration | Dr (R) | Cr (R) |
|---|---|---|---|
| 23a | **M Carey (T)** | 2 875,00 | |
| | **M Carey (B)** | | 2 875,00 |
| | *Being transfer of summons fee and collection commission (`R1 150 + R1 725`)* | | |
| 23b | **T Banks (T)** | 46 000,00 | |
| | **T Banks (B)** | | 46 000,00 |
| | *Being transfer of trust registration fees (`R8 500 balance + R37 500 withdrawn`)* | | |
| 23c | **D Johnson (T)** | 2 000,00 | |
| | **D Johnson (B)** | | 2 000,00 |
| | *Being transfer of available trust funds towards R2 300 fee (`R25 000 - R8 050 - R14 950 = R2 000`)* | | |
| *[Alt]* | *[K Hart (T) Dr R23 000 / K Hart (B) Cr R23 000 — if K Hart transfer fee is transferred]* | | |
| | **Total Month-End Transfer** | **50 875,00** *(or 73 875,00)* | **50 875,00** *(or 73 875,00)* |

#### Trust Cash Book (TCB)
| No. | Dr (Receipts) | Amount (R) | No. | Cr (Payments) | Amount (R) |
|---|---|---|---|---|---|
| 1 | K Hart (T) — Deposit | 800 000,00 | 2 | Green Bank s86(4) — K Hart | 800 000,00 |
| 4 | T Banks (T) — Deposit | 120 000,00 | 5 | Blue Bank s86(4) — T Banks | 120 000,00 |
| 7 | Blue Bank s86(4) — Withdrawal | 20 000,00 | 8 | T Banks (T) — Agent (Master's office) | 11 500,00 |
| 9 | K Hart (T) — Transfer costs | 45 000,00 | 11 | K Hart (T) — SARS Transfer Duty | 22 000,00 |
| 12 | M Carey (T) — C Rock part payment | 100 000,00 | 15 | Red Bank s86(3) — Trust investment | 2 500 000,00 |
| 14 | Obama Construction (T) — Purchase price | 5 000 000,00 | 16 | K Hart (T) — Interest (95% / or 100% R4 000) | 3 800,00 |
| 16 | Green Bank s86(4) — Capital + Interest | 804 000,00 | 16 | LPFF (T) — 5% s86(5) Interest | 200,00 |
| 17 | D Johnson (T) — Deposit | 25 000,00 | 18 | D Johnson (T) — Medical practitioner | 8 050,00 |
| 20 | Red Bank s86(3) — Withdrawal | 1 000 000,00 | 21 | D Johnson (T) — Counsel | 14 950,00 |
| 22 | Blue Bank s86(4) — Withdrawal | 37 500,00 | 23 | Business Cash Book — Month-end transfer | 50 875,00 *(or 73 875)* |
| | | | 24 | M Carey (T) — Payout (`100 000 - 2 875`) | 97 125,00 |

#### Business Cash Book (BCB)
| No. | Dr (Receipts) | Amount (R) | No. | Cr (Payments) | Amount (R) |
|---|---|---|---|---|---|
| 10 | A Keys (B) — Settlement of account | 25 875,00 | 25 | SARS — Output VAT (`150+225+6 000+3 375+300`) | 10 050,00 *(or 13 050)* |
| 23 | Trust Cash Book — Month-end transfer | 50 875,00 *(or 73 875)* | | | |

### 2. Trust & Business Ledger Accounts (Summary of Postings)
- **K Hart (T)**: Cr TCB R800 000 (1), Cr TCB R45 000 (9), Cr Interest R3 800 [or R4 000] (16); Dr TCB (SARS Transfer Duty) R22 000 (11), Dr TCB (Interest paid) R3 800 [or R4 000] (16). *(Credit balance held in Trust: R823 000,00 — or R800 000,00 if R23 000 transfer fee transferred).*
- **Green Bank s86(4) Investment (K Hart)**: Dr TCB R800 000 (2), Dr Interest R4 000 (16); Cr TCB R804 000 (16) -> Balance: Nil.
- **T Banks (T)**: Cr TCB R120 000 (4); Dr TCB (Agent) R11 500 (8), Dr T Banks (B) Transfer R46 000 (23). *(Total cash retained in TCB + s86(4) Blue Bank = R62 500,00 in Blue Bank).*
- **Blue Bank s86(4) Investment (T Banks)**: Dr TCB R120 000 (5); Cr TCB R20 000 (7), Cr TCB R37 500 (22) -> Debit balance remaining invested: R62 500,00.
- **M Carey (T)**: Cr TCB R100 000 (12); Dr M Carey (B) Transfer R2 875 (23), Dr TCB Payout R97 125 (24) -> Balance: Nil.
- **M Carey (B)**: Dr Fees & VAT R1 150 (3), Dr Fees & VAT R1 725 (13); Cr M Carey (T) Transfer R2 875 (23) -> Balance: Nil.
- **T Banks (B)**: Dr Fees & VAT R46 000 (6); Cr T Banks (T) Transfer R46 000 (23) -> Balance: Nil.
- **A Keys (B)**: Dr Fees & VAT R25 875 (10); Cr BCB R25 875 (10) -> Balance: Nil.
- **Obama Construction (T)**: Cr TCB R5 000 000 (14).
- **Red Bank s86(3) Investment**: Dr TCB R2 500 000 (15); Cr TCB R1 000 000 (20) -> Debit balance remaining invested: R1 500 000,00.
- **D Johnson (T)**: Cr TCB R25 000 (17); Dr TCB (Doctor) R8 050 (18), Dr TCB (Counsel) R14 950 (21), Dr D Johnson (B) Transfer R2 000 (23) -> Balance: Nil.
- **D Johnson (B)**: Dr Fees & VAT R2 300 (19); Cr D Johnson (T) Transfer R2 000 (23) -> Debit balance still owing by client: R300,00.
- **Fees (B)**: Cr M Carey R1 000 (3), Cr T Banks R40 000 (6), Cr A Keys R22 500 (10), Cr M Carey R1 500 (13), Cr D Johnson R2 000 (19) = Total Cr R67 000,00 *(or R87 000,00 with K Hart)*.
- **Output VAT (B)**: Cr M Carey R150 (3), Cr T Banks R6 000 (6), Cr A Keys R3 375 (10), Cr M Carey R225 (13), Cr D Johnson R300 (19) = Total Cr R10 050,00; Dr BCB (paid to SARS) R10 050,00 (25) -> Balance: Nil.

---

## QUESTION 2 [24]
- **Precedent grounding**: [[Attorneys Exam/Official Memoranda 2015-2021/AttExam20Oct2021P4A]] Q3 (Instructed Correspondent Accounting) & Scribd snippet `1068448275`.

### 1. Books of Prime Entry (Journals & Cash Books)

#### Trust Journal
| Details / Narration | Dr (R) | Cr (R) |
|---|---|---|
| **Flash Attorneys (T)** | 20 000,00 | |
| **Land Lord (T)** | | 20 000,00 |
| *Being damages collected by correspondent Flash Attorneys from debtor Never Buy (1)* | | |
| **Land Lord (T)** | 2 915,00 | |
| **Flash Attorneys (T)** | | 2 915,00 |
| *Being correspondent's fees (`R300 + R600 + R1 200 = R2 100`), VAT (`R45 + R90 + R180 = R315`), and Sheriff disbursement (`R500`) charged to client (2)* | | |

#### Fee Journal
| Details / Narration | Dr (R) | Cr (R) |
|---|---|---|
| **Flash Attorneys (B)** | 805,00 | |
| **Fees (B)** (`100 + 200 + 400`) | | 700,00 |
| **Output VAT (B)** (`15 + 30 + 60`) | | 105,00 |
| *Being 1/3 allowance on fees and VAT granted by instructed correspondent Flash Attorneys (3)* | | |

#### Transfer Journal
| Details / Narration | Dr (R) | Cr (R) |
|---|---|---|
| **Flash Attorneys (T)** | 805,00 | |
| **Flash Attorneys (B)** | | 805,00 |
| *Being transfer of 1/3 allowance from Trust to Business (2)* | | |

#### Trust Cash Book (TCB)
| Dr (Receipts) | Amount (R) | Cr (Payments) | Amount (R) |
|---|---|---|---|
| Flash Attorneys (T) — EFT received (1) | 17 890,00 | Business Cash Book — Transfer of allowance (1) | 805,00 |
| | | Land Lord (T) — Payment to client (1) | 17 085,00 |
| **Total** | **17 890,00** | **Total** | **17 890,00** |

#### Business Cash Book (BCB)
| Dr (Receipts) | Amount (R) | Cr (Payments) | Amount (R) |
|---|---|---|---|
| Trust Cash Book — Transfer of allowance (1) | 805,00 | | |

### 2. Ledger Accounts (12 marks)
- **Flash Attorneys (T)**:
  - Dr: Land Lord (T) (Cash collected) **R20 000,00** (1); Transfer to Flash Attorneys (B) **R805,00** (1) | Total Dr = **R20 805,00**
  - Cr: Land Lord (T) (Fees, VAT & Sheriff) **R2 915,00** (1); TCB (EFT received) **R17 890,00** (1) | Total Cr = **R20 805,00**
- **Land Lord (T)**:
  - Dr: Flash Attorneys (T) (Fees, VAT & Sheriff) **R2 915,00** (1); TCB (EFT payout to client) **R17 085,00** (1) | Total Dr = **R20 000,00**
  - Cr: Flash Attorneys (T) (Damages collected) **R20 000,00** (1) | Total Cr = **R20 000,00**
- **Flash Attorneys (B)**:
  - Dr: Fees & Output VAT (1/3 allowance) **R805,00** (2)
  - Cr: Flash Attorneys (T) (Transfer from Trust) **R805,00** (1)
- **Fees (B)**: Cr Flash Attorneys (B) **R700,00** (1)
- **Output VAT (B)**: Cr Flash Attorneys (B) **R105,00** (1)

---

## QUESTION 3 [12]
- **Precedent grounding**: [[Attorneys Exam/Official Memoranda 2015-2021/AttExam18Mar2021P4A]] Q2 & [[Attorneys Exam/Official Memoranda 2015-2021/AttExam5Nov2020P4A]] Q4.

### 3.1 Supplementary Business Cash Book as at 31 January 2022 [8]
| Dr (+) Receipts | Marks | Amount (R) | Cr (-) Payments | Marks | Amount (R) |
|---|---|---|---|---|---|
| EFT payment by client (Item 1) | (1) | 15 000,00 | Balance b/f (Overdraft) | (1) | 33 000,00 |
| Payment error reversal (Item 5: `1 221 - 1 212`, or Dr `1 221` / Cr `1 212`) | (2) | 9,00 | Stop order — Short-term insurance (Item 2) | (1) | 1 500,00 |
| Direct deposit by client (Item 6) | (1) | 29 491,00 | Debit order — Vehicle lease (Item 4) | (1) | 2 000,00 |
| | | | **Balance c/f (Favourable)** | (1) | **8 000,00** |
| **Total** | | **44 500,00** | **Total** | | **44 500,00** |
| **Balance b/d** | | **8 000,00** | | | |

### 3.2 Bank Reconciliation Statement as at 31 January 2022 [4]
| Description | Marks | Dr (-) (R) | Cr (+) (R) |
|---|---|---|---|
| Favourable balance as per Bank Statement | (1) | | 6 000,00 |
| Add: Outstanding cash deposit on 31 January 2022 (Item 3) | (2) | | 2 000,00 |
| **Favourable balance as per Supplementary Cash Book** | (1) | **8 000,00** | |
| **Total** | | **8 000,00** | **8 000,00** |

---

## QUESTION 4 [13]
- **Precedent grounding**: [[Attorneys Exam/Official Memoranda 2015-2021/AttExam5Nov2020P4A]] Q1.2 & [[Attorneys Exam/Official Memoranda 2015-2021/AttExam7Feb2018P3A]] Q6.2.
- **Model Answer**:
  - **4.1 Explain "Trust Reconciliation" (5 marks)**:
    - A trust reconciliation is the periodic (at least monthly/quarterly) comparison and balancing of the **total trust funds available** in the firm's Section 86(2) trust banking account (plus Section 86(3) and 86(4) trust investment accounts and trust cash on hand) (2) against the **total of all credit balances in the individual trust creditors' ledger accounts** (2), in order to verify that trust assets equal or exceed trust liabilities and that there is no trust shortfall/deficit or debit balance on any trust ledger account (1).
  - **4.2 Bank Account for Deposits (3 marks)**:
    - **4.2.1** **Trust Banking Account** (s86(2)) — money received in advance for future fees/disbursements is trust money until the work is rendered and billed (1).
    - **4.2.2** **Business Banking Account** — payment of a rendered statement of account for completed professional services belongs to the firm (1).
    - **4.2.3** **Estate Late Banking Account** (opened specifically in the name of the deceased estate under s28 of the Administration of Estates Act 66 of 1965; or if temporarily received by the firm as agent, into the Trust Banking Account before transfer to the Estate Late account) (1).
  - **4.3 Difference between a Legal Practitioner with an FFC and a Referral Legal Practitioner (5 marks)**:
    - Under the Legal Practice Act 28 of 2014 (ss34 & 84–86), a legal practitioner practising with a **Fidelity Fund Certificate (FFC)** (an attorney or a trust-account advocate under s34(2)(b)) is entitled to **accept instructions directly from members of the public** (1) and **receive, hold, and administer trust money** on behalf of clients, and must open and maintain a Section 86(2) trust banking account and undergo annual trust audits (2).
    - By contrast, a **referral legal practitioner** (an advocate practising under s34(2)(a)(i)) **may not receive or hold money or property from clients/the public**, does **not** hold a Fidelity Fund Certificate or keep a trust banking account (1), and may only render legal services **upon a brief/referral from an attorney** (except where permitted through a justice centre or Legal Aid South Africa) (1).

**TOTAL: [100]**
