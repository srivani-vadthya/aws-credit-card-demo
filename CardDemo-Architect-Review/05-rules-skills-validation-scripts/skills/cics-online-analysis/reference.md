# CICS Online Reference

## BMS ATTRB values

| Value | Meaning |
|---|---|
| ASKIP | Protected, cursor skips the field (labels, outputs) |
| PROT | Protected, cursor stops |
| UNPROT | Input-capable |
| NUM | Numeric-only input (with UNPROT) |
| BRT / NORM / DRK | Bright / normal / dark (hidden, e.g. passwords) |
| IC | Initial cursor position |
| FSET | Modified data tag set - field always returned on RECEIVE |

Other DFHMDF options: `COLOR`, `HILIGHT` (BLINK/REVERSE/UNDERLINE),
`JUSTIFY` (LEFT/RIGHT, BLANK/ZERO), `PICIN`/`PICOUT`, `GRPNAME`, `OCCURS`
(repeated rows -> list screens), `VALIDN` (MUSTFILL/MUSTENTER).

## Symbolic map suffixes

| Suffix | Meaning |
|---|---|
| L | Input length (also cursor positioning when set to -1) |
| F | Flag byte (X'80' = field erased) |
| A | Attribute byte (overrides ATTRB at SEND) |
| I | Input data |
| O | Output data |
| C/P/H/V | Color / programmed symbols / highlight / validation (EXTATT) |

The input structure is `<MAP>I`; the output structure `<MAP>O` redefines it.

## AID constants (DFHAID)

DFHENTER, DFHCLEAR, DFHPA1-3, DFHPF1-24, DFHPEN, DFHOPID, DFHMSRE,
DFHTRIG. Programs often map PF keys to actions through EVALUATE EIBAID or
through a translated "key pressed" flag set in a common routine - follow
that indirection.

## Mockup convention

```
Row/Col ruler    1        10        20        30 ...
01 | Tran: XXXX          <title literal>              Date: mm/dd/yy
02 | Prog: XXXXXXXX                                   Time: hh:mm:ss
...
- Literal text exactly as INITIAL
- Input fields: '_' x LENGTH;  output fields: 'X' x LENGTH (or '9' for NUM)
- Hidden (DRK) input: '*' x LENGTH
- Attribute byte occupies the column before POS; do not overwrite literals
```

## Pseudo-conversational checklist

- What survives between tasks: COMMAREA only (plus TSQ if used). List it.
- First-time path vs re-entry path vs return-from-called-program path.
- Who clears/initializes the COMMAREA; length passed vs expected.
- Program-to-program context fields (from/to program, from/to transid,
  last map, user id/type, selected keys, page tokens for browsing).

## Browse/list screens

Capture: browse key, direction keys (PF7/PF8 or similar), page size
(OCCURS rows on the map), first/last key retention in COMMAREA, selection
column semantics (e.g. 'S' select, 'U' update, 'D' delete), and end-of-file
messages.
