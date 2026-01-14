# httpie-hush

Hush OAuth 2 plugin for the `HTTPie <https://github.com/jkbr/httpie>` command line HTTP client.


## Installation

```bash
pipx install httpie
pipx inject httpie httpie-hush
```

You should now see `hush` under `--auth-type` in `$ http --help` output.


## Setup

```bash
httpie-hush-setup
```

Configure Hush's auth plugin with your API Key credentials (saved in `~/.httpie/config.json`).

#### Notes:
- If API Key ID is not provided in conf file it will be searched at
  `HTTPIE_HUSH_API_KEY_ID` envar
- If API Key Secret is not provided in conf file it will be searched at
  `HTTPIE_HUSH_API_KEY_SECRET` envar
- Manually inputted credentials supersede conf file and environment variables


## Usage

```bash
http --auth-type=hush GET https://api.us.hush-security.com/v1/users
```

It's possible to use an effective org by passing the ``EORG`` envar:

```bash
EORG=hush http --auth-type=hush GET https://api.us.hush-security.com/v1/users
```

