"""Test the reverb module."""

from time import sleep

from synthizer import Context, GlobalFdnReverb

from synthizer_fx.reverb import ReverbDict, reverb_from_dict, reverb_to_dict


def test_reverb_to_dict(reverb: GlobalFdnReverb) -> None:
    """Ensure we can dump to a dictionary."""
    d: ReverbDict = reverb_to_dict(reverb, name='test')
    assert d['name'] == 'test'
    assert d['gain'] == reverb.gain
    assert d['late_reflections_delay'] == reverb.late_reflections_delay
    assert d['late_reflections_diffusion'] == reverb.late_reflections_diffusion
    assert d['late_reflections_hf_reference'] == \
        reverb.late_reflections_hf_reference
    assert d['late_reflections_hf_rolloff'] == \
        reverb.late_reflections_hf_rolloff
    assert d['late_reflections_lf_reference'] == \
        reverb.late_reflections_lf_reference
    assert d['late_reflections_lf_rolloff'] == \
        reverb.late_reflections_lf_rolloff
    assert d['late_reflections_modulation_depth'] == \
        reverb.late_reflections_modulation_depth
    assert d['late_reflections_modulation_frequency'] == \
        reverb.late_reflections_modulation_frequency
    assert d['mean_free_path'] == reverb.mean_free_path
    assert d['t60'] == reverb.t60


def test_reverb_from_dict(context: Context) -> None:
    """Ensure we can load from a dictionary."""
    d: ReverbDict = {
        't60': 4.5,
        'name': 'Testing',
        'gain': 0.25,
        'late_reflections_hf_reference': 250.0
    }
    r: GlobalFdnReverb = reverb_from_dict(context, d)
    sleep(0.5)
    assert r.gain == d['gain']
    assert r.t60 == d['t60']
    assert r.late_reflections_hf_reference == d[
        'late_reflections_hf_reference'
    ]
