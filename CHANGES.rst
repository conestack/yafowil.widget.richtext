Changes
=======

2.0.1 (unreleased)
------------------

- Fix the Plone 4 richtext widget throwing a ``ReferenceError`` for every
  ``textarea.richtext``. The textarea id was referenced as undeclared ``id``
  instead of ``this.id``.
  [rnix]

- Fix the Plone 5 richtext widget creating the TinyMCE pattern twice per
  textarea. It is created once now, after the TinyMCE options request
  succeeded or failed.
  [rnix]

- Extend the JS tests to 100 % coverage, all modules including bundles are
  loaded by the tests now.
  [rnix]

- Lint and format the JS code with biome. ``make check`` runs ``biome check``,
  ``make format`` runs ``biome check --write`` (see ``include.mk``). Behavior
  unchanged.
  [rnix]

- JS tooling: Commit ``pnpm-lock.yaml``. Upgrade ``@web/test-runner`` to 1.0
  and run the JS tests headless in Chromium via Playwright, installed in the JS
  CI workflow. Drop the accidental ``install`` dev dependency. Pin patched
  versions of vulnerable transitive dependencies via ``pnpm.overrides``.
  [rnix]

- Import ``textarea_renderer`` from ``yafowil.textarea``, it is deprecated in
  ``yafowil.common``.
  [rnix]

- Modernise the code ruff flags as outdated: ``u''`` prefixes and ``.format()``
  over f-strings. Behaviour unchanged. ``super(Class, self)`` is kept, see
  ``cone.app``.
  [rnix]

- Sort the imports with ruff (one per line, ``from`` imports first, no
  sections) and format the code with ``ruff format`` (90 characters per line,
  single quotes).
  [rnix]

- Add ``qa.ruff`` domain to Makefile and pin the ruff configuration in
  ``pyproject.toml``, ``make check`` runs ``ruff check``.
  [rnix]

- Drop the Python 2 remnants: ``yafowil.compat`` usage and ``IS_PY2`` branches.
  [rnix]

- Declare ``requires-python = ">=3.10"``.
  [rnix]


2.0.0 (2026-02-03)
------------------

- Refactor package layout to use ``pyproject.toml`` and implicit namespace packages.
  [rnix]

- Rewrite JavaScript using ES6.
  [lenadax]


1.6 (2025-11-03)
----------------

- Pin upper versions of dependencies.
  [lenadax]

- Use ``yafowil.utils.as_data_attrs`` instead of deprecated
  ``yafowil.utils.generic_html5_attrs``.
  [rnix]


1.5 (2018-07-16)
----------------

- Add dedicated ``plone4`` and ``plone5`` widgets JS. TinyMCE handling is too
  different to be done generic.
  [rnix]

- Python 3 compatibility.
  [rnix]

- Convert doctests to unittests.
  [rnix]


1.4 (2017-03-01)
----------------

- Use ``yafowil.utils.entry_point`` decorator.
  [rnix, 2016-06-28]


1.3.2 (2015-01-23)
------------------

- Package cleanup.
  [rnix]

1.3.1
-----

- check for plone context in JS in order to use different tinymce
  initialization code.
  [rnix, 2012-10-25]

1.3
---

- Adopt resource providing
  [rnix, 2012-06-12]

- Provide example widget
  [rnix, 2012-06-12]

1.2
---

- fixed resources
  [rnix, 2012-03-01]

- added entry point base registration
  [agitator, 2012-02-15]

- add display mode css class
  [rnix, 2011-12-18]

1.1
---

- adopt to yafowil 1.2
  [jensens, 2011-09-20]

- make ready for z2c.autoinclude+Plone (only if available).
  [jensens, 2011-09-20]

1.0
---

- add display renderer
  [rnix, 2011-08-03]

- adopt to yafowil 1.1
  [rnix, 2011-07-08]

0.9.1
-----

- test coverage
  [rnix, 2011-05-07]

0.9
---

- made it work [rnix]
