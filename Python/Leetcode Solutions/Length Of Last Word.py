def run_pipeline(line):
    # (very) simple function pipeline
    final = line[0]()
    for f in line[1:]:
        final = f(final)
    return final
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return run_pipeline([
            lambda: s,
            self.splice,
            lambda s: s.split()[-1],
            lambda si: len(si)
        ])
    def splice(self, text):
        txit = []
        for t in text.split():
            txit += [(t.strip())]
        return " ".join(txit)