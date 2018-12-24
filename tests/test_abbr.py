# Copyright 2016 Adler Brediks Medrado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from abbr.abbr import Abbreviate
from abbr.exceptions import LanguageNotFoundError, LengthNotFoundError, LengthSizeError, PhraseNotFoundError


def test_abbreviate_params():
    phrase = "Olá Senhor Professor Doutor Jair de Lima Pinto Sobrinho, como vai, tudo bem?"  # noqa
    abbr = Abbreviate(phrase, 40, 'pt_br')
    assert abbr.phrase == phrase
    assert abbr.language == 'pt_br'
    assert abbr.length == 40
    assert abbr.length > 0


def test_abbreviate_params_phrase_not_null_exception():
    with pytest.raises(PhraseNotFoundError):
        Abbreviate('', 40, 'pt_br')


def test_abbreviate_params_language_not_null_exception():
    with pytest.raises(LanguageNotFoundError):
        phrase = "Olá Senhor Professor Doutor Jair de Lima Pinto Sobrinho, como vai, tudo bem?"  # noqa
        Abbreviate(phrase, 40, '')


def test_abbreviate_params_length_not_null_exception():
    with pytest.raises(LengthNotFoundError):
        phrase = "Olá Senhor Professor Doutor Jair de Lima Pinto Sobrinho, como vai, tudo bem?"  # noqa
        Abbreviate(phrase, '', 'pt_br')


def test_abbreviate_params_length_must_be_greater_than_zero():
    with pytest.raises(LengthSizeError):
        phrase = "Olá Senhor Professor Doutor Jair de Lima Pinto Sobrinho, como vai, tudo bem?"  # noqa
        Abbreviate(phrase, 0, 'pt_br')


def test_abbreviation_replace():
    phrase = "Olá Senhor Professor Doutor Jair de Lima Pinto Sobrinho, como vai, tudo bem?"  # noqa
    abbr = Abbreviate(phrase, 40, 'pt_br')
    abbr.do_abbreviation()
    abbr.truncate_phrase()
    assert abbr.new_phrase == "Olá Sr. Prof. Dr. Jair de Lima Pinto Sob"
    assert len(abbr.new_phrase) == 40
