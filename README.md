# envmigrate

Helper script to migrate environment variables between resin.io apps using the SDK.

## Usage

This script requires Python 2.7 (due to the requirements of the resin.io SDK).
Install the dependencies with `pip install -r requirements.txt`. After that
run the script:

```
$./envmigrate.py --help
Usage: envmigrate.py [OPTIONS]

  Migrate environment variables from one resin.io app to another, optionally
  removing variables from the target that do not exist at the origin.

Options:
  -f, --from INTEGER  ID of application to copy env vars from  [required]
  -t, --to INTEGER    ID of application to copy env vars to  [required]
  --token TEXT        Resin.io auth token, can specify it with the RESIN_TOKEN
                      env var as well  [required]
  --delete-extra      Toggles deleting extra environment variables in the
                      receiving app
  -q, --quiet         Toggles hiding process details
  --yes               Confirm the action without prompting.
  --help              Show this message and exit.
```

For example:

```
$./envmigrate.py -f 129771 -t 129772 --delete-extra
Are you sure you want to copy the env vars? [y/N]: y
Logged in user: imrehg
Updating ENVVAR -> XYZ
Updating RESIN_SUPERVISOR_DELTA -> 1
Deleting TOOMUCH
```

## License

Copyright 2016 Resin.io

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
