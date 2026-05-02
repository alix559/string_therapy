/**
 * Canonical source: ``appspecifications.ipynb`` (``STRING_THERAPY_UI_QNT``).
 * Abstract session model for the string_therapy web UI: dock icons **1** and **4**,
 * optional ``notebook_known`` after a successful chat → notebook injection (mirrors
 * ``SESSION_NOTEBOOK_KEY`` being meaningful).
 *
 * CLI: ``quint verify string_therapy/quint_specs/string_therapy_ui.qnt --invariants activeIconImplementedInv``
 */
module string_therapy_ui {

  pure val ICON1: int = 1
  pure val ICON4: int = 4
  pure val DOCK: Set[int] = Set(ICON1, ICON4)

  /// Expanded visualization (dock selection).
  var active: int
  /// Session has pinned notebook context for chat injection.
  var notebook_known: bool

  val state = { active: active, notebook_known: notebook_known }

  action init: bool = all {
    active' = ICON4,
    notebook_known' = false,
  }

  action open_lab: bool = all {
    active' = ICON4,
    notebook_known' = notebook_known,
  }

  action open_icon1: bool = all {
    active' = ICON1,
    notebook_known' = notebook_known,
  }

  action remember_notebook: bool = all {
    active' = active,
    notebook_known' = true,
  }

  action step: bool = any {
    open_lab,
    open_icon1,
    remember_notebook,
  }

  val activeIconImplementedInv: bool = active.in(DOCK)
}
