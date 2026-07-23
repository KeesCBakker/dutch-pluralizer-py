# CLI Reference

The `dutch-pluralizer` package provides a command-line interface for
pluralizing and singularizing Dutch words using Hunspell.

## Usage

```
python -m dutch_pluralizer [options] <word>
```

## Options

| Flag | Description |
|------|-------------|
| `-h`, `--help` | Show help message and exit |
| `-p`, `--pluralize` | Pluralize the word (default if no flag given) |
| `-s`, `--singularize` | Singularize the word |
| `-pa`, `--pluralize_advanced` | Show detailed pluralization output |
| `-sa`, `--singularize_advanced` | Show detailed singularization output |
| `-v`, `--verbose` | Show an error message when a word could not be processed |

If no flag is given, pluralize is used as the default action.

## Examples

### Basic pluralization

Pluralize a Dutch noun:

```
$ python -m dutch_pluralizer -p kaas
kazen
```

The default action is also pluralize:

```
$ python -m dutch_pluralizer kaas
kazen
```

### Basic singularization

Reverse a plural back to its singular form:

```
$ python -m dutch_pluralizer -s kazen
kaas
```

### Advanced pluralization

Shows the algorithmic result, final plural, and Hunspell corrections:

```
$ python -m dutch_pluralizer -pa album
{'algorithmic_plural': 'alba',
 'hunspell_spelled': True,
 'plural': 'albums',
 'suggestions': ('Alba',
                 'aba',
                 'balba',
                 'albe',
                 'alia',
                 'alla',
                 'alma',
                 'alfa',
                 'Elba'),
 'switched_ending_from': 'a',
 'switched_ending_to': 'ums'}
```

Fields explained:

- **algorithmic_plural** — what the rule-based algorithm produced before Hunspell correction
- **plural** — the final result after Hunspell correction
- **hunspell_spelled** — whether the algorithmic result was recognized by Hunspell
- **switched_ending_from / switched_ending_to** — if the ending was swapped (e.g., `-a` → `-ums`)
- **suggestions** — spelling suggestions from Hunspell

### Advanced singularization

Shows detailed singularization info:

```
$ python -m dutch_pluralizer -sa kazen
{'algorithic_singular': ['kaas'],
 'could_be_plural': True,
 'hunspell_spelled': True,
 'singular': 'kaas',
 'suggestions': ()}
```

### Verbose mode

When a word cannot be processed, no output is shown by default. Use `-v` to
see an error message:

```
$ python -m dutch_pluralizer -v -p xyzzy
Could not pluralize 'xyzzy'.
```
